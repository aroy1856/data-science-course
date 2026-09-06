# Assignment 30 - Groq RAG + Streamlit Chat

ChatGroq RAG over a doc (`Book1.txt` / uploaded pdf-txt), then a Streamlit chat UI with history.

## How to run

**Notebook**
1. open `groq.ipynb`
2. keep `Book1.txt` in this folder
3. run top to bottom
4. `.env` needs `GROQ_API_KEY` + `OPENAI_API_KEY` (embeddings)

**Streamlit app**
```bash
cd genai/langchain/assignment-30
streamlit run app.py
```
upload a pdf/txt → ask grounded questions in the chat box

needs: langchain-groq, langchain-openai, langchain-chroma, langchain-community, langchain-text-splitters, streamlit, python-dotenv

## What I did

**part 1 — groq setup**
- `ChatGroq(model="openai/gpt-oss-20b", max_tokens=512)` (free-tier friendly; avoid huge default max_tokens)
- smoke test: capital of France

**part 2 — rag backend (notebook)**
- `TextLoader("Book1.txt")` → recursive split (`1000` / `200`)
- OpenAI embeddings → Chroma → retriever
- context-only prompt → LCEL: retriever | prompt | Groq | string
- tested “What is Hogwarts?”

**part 3–4 — streamlit**
- `app.py`: file upload, chunk + chroma, history-aware rewrite, grounded answer
- chat UI with `st.chat_input` / `st.chat_message`
- history in `st.session_state` + `RunnableWithMessageHistory`

**task 11 — insights**
- why Groq for RAG chat, Groq vs OpenAI RAG, why Streamlit for prototypes

## Where I struggled

- Groq 429 if `max_tokens` > free OTPM — keep it low (e.g. 512)
- `llama3.2:3b` is an Ollama id, not a Groq model — use something like `openai/gpt-oss-20b`
- Streamlit chat: don’t pass `on_submit=bot.invoke`; check `if user_input:` then invoke with `session_id` config
- `store = {}` resets every Streamlit rerun — must use `st.session_state`
- terminal spammed `torchvision` missing from Streamlit watching `transformers` — noisy, not the RAG bug
- embeddings still need OpenAI even though chat is Groq

## Files

- `groq.ipynb` — notebook (RAG pipeline + writeups)
- `app.py` — Streamlit Groq RAG chat
- `Book1.txt` — sample doc
- `requirements.txt` — deps
- `README.md` — this file
