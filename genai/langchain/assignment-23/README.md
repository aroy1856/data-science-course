# Assignment 23 - RAG (Retrievers + YouTube Chatbot)

LangChain RAG: OpenAI chat, Wikipedia + FAISS retrievers, MMR / multi-query / compression, then a YouTube transcript Q&A chain.

## How to run

1. open `rag.ipynb`
2. run top to bottom
3. put `OPENAI_API_KEY` in the repo `.env`

needs: langchain-openai, langchain-community, langchain-classic, langchain-text-splitters, faiss, youtube-transcript-api, wikipedia, python-dotenv

YouTube cells need network. if `add_video_info=True` blows up with HTTP 400, turn it off — transcript still loads.

## What I did

**part 1 — openai setup**
- load key from `.env`
- `ChatOpenAI(model="gpt-4o-mini")` smoke test

**part 2 — retrievers**
- `WikipediaRetriever` (“How LLM works?”)
- AcmeMart docs → OpenAI embeddings → FAISS → similarity retriever

**part 3 — advanced retrieval**
- MMR (`search_type="mmr"`) + note on diversity vs plain similarity
- `MultiQueryRetriever` — LLM rewrites query, better recall
- `ContextualCompressionRetriever` + `LLMChainExtractor` — trim chunk noise

**part 4 — youtube rag**
- `YoutubeLoader` on `UpE5yuhwXXc`, split (`chunk_size=1000`, overlap=200)
- FAISS vector store + retriever
- LCEL chain: retriever → prompt → llm → string (answers only from transcript / “don’t know”)
- tested 6 questions (topic, explanation, speaker, guests, etc.)

**part 5 — insights**
- RAG vs normal prompting, why vector stores, MMR vs similarity, multi-query + compression

## Where I struggled

- YouTube `add_video_info=True` → HTTP 400 (metadata fetch). transcript works without it
- MMR / retriever sometimes need `search_kwargs=` not `kwargs=` or settings get ignored
- multi-query + compression = extra LLM calls (slower / costlier)
- wikipedia + youtube need network

## Files

- `rag.ipynb` — main notebook
- `README.md` — this file
