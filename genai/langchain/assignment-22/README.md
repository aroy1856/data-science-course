# Assignment 22 - Embeddings & Vector Stores

LangChain embeddings + similarity search. OpenAI / Hugging Face / Ollama backends, then FAISS + Chroma, wrapped in a tiny search pipeline.

## How to run

1. open `embedding.ipynb`
2. run top to bottom
3. put `OPENAI_API_KEY` in the repo `.env` (loaded via `python-dotenv`)

needs: langchain-openai, langchain-community, langchain-huggingface, langchain-ollama, faiss-cpu (or faiss), chromadb, scikit-learn, sentence-transformers

**Ollama (task 6)**
- install + start Ollama locally
- `ollama pull nomic-embed-text`
- skip those cells if Ollama isn’t running

## What I did

**part 1 — embedding models**
- sample AcmeMart policy docs (`Document` list)
- OpenAI `text-embedding-3-small` with `dimensions=128`
- Hugging Face `sentence-transformers/all-MiniLM-L6-v2` (384-dim)
- task 3 writeup: when to pick OpenAI vs HF, cost vs speed

**part 2 — similarity search**
- manual `search()` with cosine similarity over in-memory OpenAI vectors
- tested 3 queries (return / shipping / payment)
- FAISS via `FAISS.from_documents` + `similarity_search`

**part 3 — Ollama**
- `OllamaEmbeddings(model="nomic-embed-text")` on the same docs
- compared dims / local vs cloud with OpenAI

**part 4 — vector stores**
- FAISS: build, search, `save_local` / `load_local`, verified same doc ids
- Chroma: `persist_directory="chroma_db"`, then reload + search
- task 9: FAISS vs Chroma (in-memory/save vs persistent DB)

**part 5 — pipeline + insights**
- `DocumentSearchPipeline` with switchable embedding + vector store
- demo: OpenAI + FAISS → return-policy search
- task 11: why embeddings, why vector DBs, how this feeds RAG

## Where I struggled

- Chroma returned `[]` at first — `from_documents` writes default collection `"langchain"`, but reopening with a different `collection_name` opens an empty collection. Fix: reload without a wrong name (or pass the same `collection_name` both times). `persist_directory` is the folder, not the collection.
- HF first run downloads the model — slow once, then fine
- Ollama cells need the daemon up + model pulled
- FAISS reload needs `allow_dangerous_deserialization=True`

## Files

- `embedding.ipynb` — main notebook
- `faiss_index.faiss/` — saved FAISS index (from notebook)
- `chroma_db/` — persisted Chroma store
- `README.md` — this file
