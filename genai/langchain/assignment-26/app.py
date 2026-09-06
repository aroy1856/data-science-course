import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger("groq-app")

app = FastAPI(title="Groq Chatbot API", version="0.1.0")


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User question")


class ChatResponse(BaseModel):
    answer: str


if not os.getenv("GROQ_API_KEY"):
    logger.warning("GROQ_API_KEY is not set")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    max_tokens=512,
)

# must include {question} or the user message never reaches the model
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer clearly and concisely."),
        ("human", "{question}"),
    ]
)

chat_chain = prompt | llm | StrOutputParser()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        logger.info("chat request: %s", request.question[:120])
        answer = chat_chain.invoke({"question": request.question})
        return ChatResponse(answer=answer)
    except Exception as e:
        logger.exception("chat failed")
        raise HTTPException(status_code=500, detail=str(e)) from e
