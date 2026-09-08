# Assignment 34 - Text Summarization (Stuff / Map-Reduce / Refine)

LangChain summarization: prompt-only, stuff chain, map-reduce, refine — then a small `summarize_document()` switcher.

## How to run

1. open `text_ummarization.ipynb`
2. keep `attention.pdf` next to the notebook (Attention Is All You Need)
3. run top to bottom
4. put `OPENAI_API_KEY` in repo `.env`

needs: langchain-openai, langchain-community, langchain-classic, langchain-text-splitters, pypdf, python-dotenv

## What I did

**part 1 — prompt summarization**
- `PyPDFLoader('attention.pdf')`
- basic `PromptTemplate` → `gpt-4o-mini`
- variations: 5–6 line summary vs bullet points

**part 2 — stuff chain**
- `load_summarize_chain(llm, chain_type="stuff")`
- conceptual notes: one-shot dump into context; good only if doc fits

**part 3 — map-reduce**
- split with `RecursiveCharacterTextSplitter(1000/200)`
- `chain_type="map_reduce"`
- peeked at chain pieces / keys

**part 4 — refine**
- `chain_type="refine"` iterative summary
- compared all four methods (quality / coherence / long-doc fit)

**part 5 — mini project**
- `summarize_document(text, method=...)` with `prompt|stuff|map_reduce|refine`
- task 14 insights: long docs, speed vs quality, real use cases

## Where I struggled

- stuff/prompt choke on long PDFs (context window) — need map-reduce/refine
- `load_summarize_chain` lives in `langchain_classic` now (not old `langchain.chains`)
- map-reduce / refine = many LLM calls → slower + costlier
- filename typo `text_ummarization.ipynb` (missing “s”) — left as-is

## Files

- `text_ummarization.ipynb` — notebook
- `attention.pdf` — source paper (if present) / also `Book1.txt` in folder
- `README.md` — this file
