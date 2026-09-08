# Assignment 38 - CodeLlama Code Assistant (Ollama)

Local code helper with `codellama:7b` via Ollama + LangChain: generate / explain / debug / optimize — notebook + Streamlit UI.

## How to run

**Pull model (once)**
```bash
ollama pull codellama:7b
ollama list
```

**Notebook**
1. open `codellama.ipynb`
2. run top to bottom (needs Ollama running)

**Streamlit app**
```bash
cd genai/langchain/assignment-38
streamlit run app.py
```

needs: langchain-ollama, langchain-core, streamlit, ollama + `codellama:7b`

## What I did

**task 1 — setup**
- Ollama installed locally
- pulled `codellama:7b`
- notebook cell asserts model shows up in `ollama list`

**task 2 — basic ChatOllama**
- `ChatOllama(model="codellama:7b", temperature=0.1)`
- smoke prompts: prime-number function + explain a tiny `add`

**task 3 + 5 — assistant helpers + prompt templates**
- `ChatPromptTemplate` per task: generate / explain / debug / optimize
- wrappers: `generate_code`, `explain_code`, `debug_code`, `optimize_code`
- structured outputs (fenced code + short notes / walkthrough / bugs / opts)

**task 4 — Streamlit**
- `app.py`: text area + task dropdown + Run button
- same four templates → CodeLlama → markdown output

## Where I struggled

- must pull the model first or every invoke fails / hangs
- CodeLlama can be slow on CPU — keep prompts short while testing
- without task-specific system prompts, answers get messy; templates keep generate/explain/debug/optimize consistent

## Files

- `codellama.ipynb` — notebook (tasks 1–3, 5)
- `app.py` — Streamlit code assistant
- `README.md` — this file
