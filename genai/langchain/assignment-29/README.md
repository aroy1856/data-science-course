# Assignment 29 - OpenAI vs Ollama Q&A App

Same Q&A prompt, two backends: OpenAI + local Ollama, then a tiny Streamlit switcher.

## How to run

**Notebook**
1. open `qna_app.ipynb`
2. run top to bottom
3. `.env` needs `OPENAI_API_KEY`
4. Ollama running locally + a model pulled (I used `llama3.2:3b`)

```bash
ollama pull llama3.2:3b
ollama list
```

**Streamlit app**
```bash
cd genai/langchain/assignment-29
streamlit run app.py
```

needs: langchain-openai, langchain-ollama, streamlit, python-dotenv

## What I did

**part 1 — openai q&a**
- `ChatOpenAI(model="gpt-4o-mini")`
- basic `ChatPromptTemplate` (system + human `{question}`)
- tested 5 questions (LLM, LangChain, OpenAI vs Ollama, TPU, …)
- optional multi-turn with `MessagesPlaceholder` + `RunnableWithMessageHistory` (name follow-up)

**part 2 — ollama**
- `ChatOllama(model="llama3.2:3b")` + same prompt style
- compared a few answers side by side

**task 6 — compare**
- quality / latency / cost / privacy notes (OpenAI stronger hosted quality; Ollama private + free local)

**part 3 — unified app**
- `get_answer(question, model_type="openai"|"ollama")`
- Streamlit UI in `app.py` — sidebar model pick + text box

**task 9 — insights**
- when to pick OpenAI vs open-source, prod tradeoffs, cost/scale

## Where I struggled

- Ollama must be running or `ChatOllama` just fails / hangs
- after the multi-turn cell, `prompt` got overwritten to the history version (`{input}` + `chat_history`) — simple ollama/openai chains need the basic `{question}` prompt again (or rebuild it like in `app.py`)
- small local models answer fine for short Q&A but feel weaker/less consistent than `gpt-4o-mini`

## Files

- `qna_app.ipynb` — notebook
- `app.py` — Streamlit chatbot (OpenAI / Ollama switch)
- `README.md` — this file
