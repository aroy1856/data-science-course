# Assignment 26 - Groq Chat + FastAPI

Groq LLM via LangChain, tiny RAG over a wiki page, then a FastAPI `/chat` wrapper.

## How to run

**Notebook**
1. open `groq.ipynb`
2. run top to bottom
3. `.env` needs `GROQ_API_KEY` (and `OPENAI_API_KEY` for the RAG embeddings part)

**API**
```bash
cd genai/langchain/assignment-26
uv run uvicorn app:app --reload
```
- health: http://127.0.0.1:8000/health
- docs: http://127.0.0.1:8000/docs
- chat: `POST /chat` with `{"question": "..."}`

needs: langchain-groq, fastapi, uvicorn, langchain-chroma, langchain-openai, requests, python-dotenv

## What I did

**part 1 — groq chat**
- `ChatGroq(model="openai/gpt-oss-20b")` (llama3 ids werent on my key)
- `groq_chat()` with system + user `ChatPromptTemplate`, tested a bunch of AI/python questions

**part 2 — groq rag**
- loaded LLM wiki via `WebBaseLoader`, split, OpenAI embeddings → Chroma
- LCEL: retriever → grounded prompt → Groq → string
- context-only prompt: LLM uses get answered, “capital of France” correctly says not in context

**part 3–4 — fastapi**
- `app.py`: `GET /health`, `POST /chat` with Pydantic request/response
- env keys + basic logging + `requirements.txt`
- tested from notebook with `requests`

**part 5 — demo + insights**
- hit `/chat` with multiple questions, checked status/latency/answers
- task 10: why Groq for realtime, vs OpenAI latency, why API-first

## Where I struggled

- `qwen/qwen3.8-27b` 429 OTPM: default `max_tokens=2048` but free tier OTPM ~1000 — set `max_tokens=512` or switch model
- classic `llama-3.1-8b-instant` not on my Groq account — used `openai/gpt-oss-20b`
- first FastAPI prompt had no `{question}` so model ignored the user text and replied with filler — fixed in `app.py`
- RAG needs OpenAI embeddings key even though chat is Groq

## Files

- `groq.ipynb` — notebook
- `app.py` — FastAPI + Groq chat
- `requirements.txt` — deps for the API
- `README.md` — this file
