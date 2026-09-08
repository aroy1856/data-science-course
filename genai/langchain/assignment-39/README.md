# Assignment 39 - Deploy GenAI App (Streamlit Cloud + HF Spaces)

Deployed the **Text-to-Math Agent** (`app.py`, same as assignment-35) to Streamlit Cloud and Hugging Face Spaces.

Word problems → `create_agent` + calculator tool → answer, with chat history in `session_state`. Uses OpenAI `gpt-4o-mini` via `OPENAI_API_KEY` (secrets on cloud).

## How to run locally

```bash
cd genai/langchain/assignment-39
streamlit run app.py
```

needs: see `requirements.txt` + `OPENAI_API_KEY` in `.env`

## What I did

**task 1 — Streamlit Cloud**
- GitHub has `app.py` + `requirements.txt`
- Streamlit Cloud main file: `genai/langchain/assignment-39/app.py`
- secret: `OPENAI_API_KEY`
- tested live URL (word problems + follow-ups + clear history)

**task 2 — Hugging Face Spaces**
- Streamlit Space + same files
- Space README YAML (`sdk: streamlit`, `app_file: app.py`)
- secret: `OPENAI_API_KEY`
- tested Space URL

**task 3 — compare**
- Streamlit Cloud = simplest for pure Streamlit + GitHub
- HF Spaces = better for ML demos / Gradio / Docker / discovery next to models
- use Streamlit Cloud for course/data apps; HF Spaces for public model demos

## Where I struggled

- Streamlit Cloud main-file path must be the nested monorepo path
- HF Spaces needs the YAML README header or the build won’t treat it as Streamlit
- cloud needs `OPENAI_API_KEY` in secrets (local `.env` isn’t uploaded)

## Files

- `app.py` — Text-to-Math Agent (assignment-35 app)
- `requirements.txt` — cloud deps
- `deployment.ipynb` — deployment notes + comparison
- `README.md` — this file
