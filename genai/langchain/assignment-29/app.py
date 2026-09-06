import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
if os.getenv("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY is not set")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm_openai = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
llm_ollama = ChatOllama(model="llama3.2:3b", temperature=0.2)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions."),
    ("human", "{question}"),
])
chain_openai = prompt | llm_openai
chain_ollama = prompt | llm_ollama


def get_answer(question, model_type="openai"):
    if model_type == "openai":
        response = chain_openai.invoke({"question": question})
    elif model_type == "ollama":
        response = chain_ollama.invoke({"question": question})
    else:
        raise ValueError(f"Invalid model type: {model_type}")
    return response.content
st.title("Q&A Chatbot")

question = st.text_input("Enter your question")

st.sidebar.title("Select Model")
model_type = st.sidebar.selectbox("Select model type", ["openai", "ollama"])

if st.button("Get Answer"):
    if model_type == "openai":
        answer = chain_openai.invoke({"question": question})
    elif model_type == "ollama":
        answer = chain_ollama.invoke({"question": question})
    else:
        st.error("Invalid model type")
        raise ValueError(f"Invalid model type: {model_type}")
    st.write(answer.content)