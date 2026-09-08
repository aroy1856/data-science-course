# Assignment 37 - AstraDB PDF RAG Q&A

PDF RAG on DataStax AstraDB: `hp1.pdf` → split → OpenAI embeddings → Astra vector store → retriever → grounded LLM answers.

## How to run

1. open `rag_qna.ipynb`
2. keep `hp1.pdf` next to the notebook
3. put in repo `.env`:
   - `OPENAI_API_KEY`
   - `ASTRA_DB_API_ENDPOINT`
   - `ASTRA_DB_APPLICATION_TOKEN`
4. run top to bottom — Task 4 does `clear()` then `add_documents` **once**

needs: langchain-openai, langchain-astradb, langchain-community, langchain-text-splitters, pypdf, python-dotenv

## What I did

**task 1–2 — Astra setup / connect**
- Astra vector DB + app token / endpoint in `.env`
- `AstraDBVectorStore(..., collection_name="pdf_rag")` with OpenAI embeddings

**task 3 — load & split**
- `PyPDFLoader("hp1.pdf")`
- `RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)` → ~455 chunks

**task 4 — store embeddings**
- `vstore.clear()` first (don’t use `delete()` with no ids)
- `add_documents(chunks)` once
- `similarity_search` smoke check

**task 5 — RAG pipeline**
- retriever `k=6` → `format_docs` → chat prompt with `{context}` / `{question}` → `gpt-4o-mini`
- system: answer only from context; else exact `I don't know`

**task 6 — testing**
- in-doc: Dursleys’ address, who left baby Harry, Hogwarts, Hagrid tells Harry he’s a wizard, Hagrid’s dog
- out-of-context: capital of France → don’t know

## Where I struggled

- re-running `add_documents` duplicates rows — always `clear()` before a fresh load
- `vstore.delete()` without ids raises `ValueError` — use `clear()`
- vague questions (“Who is Harry Potter?”) often miss the right chunks even when the book has the answer

## Files

- `rag_qna.ipynb` — notebook
- `hp1.pdf` — source PDF
- `README.md` — this file
