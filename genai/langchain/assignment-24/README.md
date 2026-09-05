# Assignment 24 - Ollama + LangSmith

Local Ollama chat via LangChain, with LangSmith tracing on.

## How to run

1. start Ollama locally (`ollama serve` if needed)
2. pull a model if missing, e.g. `ollama pull deepseek-r1`
3. put LangSmith keys in repo-root `.env`:
   - `LANGSMITH_TRACING=true`
   - `LANGSMITH_API_KEY=...`
   - `LANGSMITH_PROJECT=ollama-chatbot`
4. open `ollama.ipynb`, run top to bottom

needs: langchain-ollama, python-dotenv, langsmith, ollama running locally

**tracing tip:** call `load_dotenv()` *before* importing langchain/ollama — langsmith caches env, so loading after import leaves tracing off.

## What I did

**task 1 — ollama + langsmith**
- `OllamaLLM(model="deepseek-r1")`
- prompts: capital of France, tell me about yourself
- LangSmith project `ollama-chatbot` — screenshot in notebook + `image.png`

## Where I struggled

- LangSmith showed no traces at first: imported langchain before `load_dotenv()`, so tracing stayed False
- need Ollama daemon up + model pulled (`ollama list`)

## Files

- `ollama.ipynb` — notebook (includes LangSmith screenshot)
- `image.png` — LangSmith UI screenshot
- `README.md` — this file
