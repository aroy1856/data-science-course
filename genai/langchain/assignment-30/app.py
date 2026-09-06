import os 
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.runnables import RunnableLambda
from operator import itemgetter
from dotenv import load_dotenv
from langchain_chroma import Chroma
load_dotenv()
if os.getenv("GROQ_API_KEY") is None:
    raise ValueError("GROQ_API_KEY is not set")
else:
    print("GROQ_API_KEY is set")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=512,
)

st.title("Groq Chatbot")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
os.makedirs("uploads", exist_ok=True)

file = st.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])
if file:
    file_path = os.path.join("uploads", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getvalue())
    st.success(f"File uploaded successfully to {file_path}")
    documents = []
    if file.type == "application/pdf":
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    elif file.type == "text/plain":
        loader = TextLoader(file_path)
        documents.extend(loader.load())

    all_splits = text_splitter.split_documents(documents)
    st.write(f"Total number of chunks: {len(all_splits)}")
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=embeddings)
    st.write(f"Vectorstore created successfully")
    retriever = vectorstore.as_retriever()
    st.write(f"Retriever created successfully")

    ctx_query_template = ChatPromptTemplate.from_messages([
        (
            "system",
            "Reformulate the user's question as a standalone question "
            "using the conversation history. "
            "If the question is already standalone, return it unchanged."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    ctx_query_chain = ctx_query_template | llm | StrOutputParser()

    ans_template = ChatPromptTemplate.from_messages([
        (
            "system",
            """Answer the user's question using ONLY the provided context.

            If the answer cannot be found in the context, say:
            "I don't know based on the provided context."

            Context:
                {context}
            """
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def get_context(x):
        if x["chat_history"]:
            standalone_question = ctx_query_chain.invoke({
                "input": x["input"],
                "chat_history": x["chat_history"],
            })
        else:
            standalone_question = x["input"]
        return format_docs(retriever.invoke(standalone_question))

    chain = (
        {
            "context": RunnableLambda(get_context),
            "chat_history": itemgetter("chat_history"),
            "input": itemgetter("input"),
        }
        | ans_template
        | llm
        | StrOutputParser()
    )

    if "chat_store" not in st.session_state:
        st.session_state.chat_store = {}
    if "messages" not in st.session_state:
        st.session_state.messages = []

    def get_chat_history(session_id: str):
        if session_id not in st.session_state.chat_store:
            st.session_state.chat_store[session_id] = InMemoryChatMessageHistory()
        return st.session_state.chat_store[session_id]

    bot = RunnableWithMessageHistory(
        chain,
        get_chat_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )

    # render prior turns
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask me anything about the uploaded file")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = bot.invoke(
                    {"input": user_input},
                    config={"configurable": {"session_id": "streamlit-user"}},
                )
                st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.info("Upload a PDF or TXT file to start chatting.")