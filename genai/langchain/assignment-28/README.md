# Assignment 28 - Conversational RAG Q&A

Doc RAG with chat memory: load `Book1.txt` (Harry Potter letter-ish text) → chunk → Chroma → retrieve → prompt with `MessagesPlaceholder` → LLM, plus trimming + multi-turn tests.

## How to run

1. open `rag_qna.ipynb`
2. keep `Book1.txt` next to the notebook
3. run top to bottom
4. put `OPENAI_API_KEY` in repo `.env`

needs: langchain-openai, langchain-community, langchain-text-splitters, langchain-chroma, chromadb, python-dotenv

## What I did

**part 1 — ingest**
- `TextLoader("Book1.txt")`
- `RecursiveCharacterTextSplitter` → chunks

**part 2 — vector store**
- OpenAI embeddings (`text-embedding-3-small`)
- Chroma index + retriever

**part 3–4 — conversational RAG**
- prompt: system (context-only) + `MessagesPlaceholder("chat_history")` + human `{question}` / `{input}`
- LCEL: `itemgetter(...) | retriever | format_docs` → prompt → llm → string
- wrap with `RunnableWithMessageHistory` + `InMemoryChatMessageHistory` keyed by `session_id`
- trimmer: `trim_messages(max_tokens=1000, strategy="last")` on history before the prompt

**part 5–6 — testing**
- multi-turn: where Harry lives → who tells him he’s a wizard
- bigger follow-up list (friends / house / owl / “what house is he in?” etc.) on `ses3`

**task 11 — insights**
- normal vs conversational RAG, why history matters for follow-ups, long-memory tradeoffs, trimming impact

## Where I struggled

- first tried `RunnableWithMessageHistory(InMemoryChatMessageHistory())` *inside* the input dict → `TypeError` missing `get_session_history`. fix: build RAG chain first, wrap once on the outside
- need `config={"configurable": {"session_id": "..."}}` or history never sticks
- prompt keys must match (`input` vs `question`) with `input_messages_key`
- follow-ups that are too vague can still miss if retrieval doesn’t pull the right chunk — history helps but isn’t magic

## Files

- `rag_qna.ipynb` — main notebook
- `Book1.txt` — source doc
- `README.md` — this file
