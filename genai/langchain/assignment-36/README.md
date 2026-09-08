# Assignment 36 - HuggingFace + LangChain

Load an HF Inference model through LangChain, wire it into a prompt chain, then compare plain vs chat prompt templates.

## How to run

1. open `huggingface.ipynb`
2. put `HF_TOKEN` (or `HUGGINGFACEHUB_API_TOKEN`) in repo `.env`
3. run top to bottom

needs: langchain-huggingface, langchain-core, python-dotenv, huggingface_hub

## What I did

**part 1 — load HF model**
- `HuggingFaceEndpoint` + `ChatHuggingFace` (instruct models need `task="conversational"`)
- used `openai/gpt-oss-20b` — Mistral-7B was chat-only *and* not on providers enabled for my token
- simple invoke: `What is LangChain?`

**part 2 — HF inside a LangChain chain**
- `ChatPromptTemplate.from_template(...) | llm`
- same HF chat model, multiple prompts via `{input}`

**part 3 — ChatPromptTemplate (system + human)**
- `ChatPromptTemplate.from_messages([("system", ...), ("human", "{input}")])`
- invoke through HF-backed `llm`
- compared vs plain `from_template`: roles stay separated for chat models; plain template dumps instructions into one user blob

## Where I struggled

- bare `HuggingFaceEndpoint` defaults to `text-generation` → fails on conversational/instruct models
- fix = wrap with `ChatHuggingFace` + `task="conversational"`
- model availability depends on HF token / enabled providers (Mistral failed; gpt-oss-20b worked)

## Files

- `huggingface.ipynb` — notebook
- `README.md` — this file
