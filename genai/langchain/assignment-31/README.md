# Assignment 31 - Conversational PDF Q&A

PDF RAG with chat memory: load `hp1.pdf` → chunk → Chroma → retrieve → prompt + `MessagesPlaceholder` → LLM, with history trimming + multi-turn Harry Potter tests.

## How to run

1. open `rag_qna.ipynb`
2. keep `hp1.pdf` next to the notebook
3. run top to bottom
4. put `OPENAI_API_KEY` in repo `.env`

needs: langchain-openai, langchain-community, langchain-text-splitters, langchain-chroma, pypdf, python-dotenv

## What I did

**part 1 — pdf ingest**
- `PyPDFLoader("hp1.pdf")`
- `RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)`

**part 2 — embeddings / store**
- OpenAI `text-embedding-3-small` + `ChatOpenAI(gpt-4o-mini)`
- Chroma index → retriever

**part 3–4 — conversational RAG**
- prompt: system (PDF context only / “I don’t know”) + `MessagesPlaceholder("chat_history")` + human question
- LCEL retrieve → prompt → llm → string
- `RunnableWithMessageHistory` + in-memory store keyed by `session_id`
- `trim_messages(max_tokens=1000, strategy="last")` on history before the prompt

**part 5–6 — testing**
- follow-ups: where Harry lives → who tells him he’s a wizard
- bigger multi-turn list (friends / house / owl / “what house is he in?” …) on `ses3`

**task 11 — insights**
- PDF Q&A vs conversational, why history matters, long-memory tradeoffs, trimming impact

## Where I struggled

- need `config={"configurable": {"session_id": "..."}}` or history never sticks
- prompt key (`input` vs `question`) must match `input_messages_key`
- PDF text can be messy / long — chunking matters a lot for retrieval quality
- trimming helps cost/latency but can drop older entities if the follow-up depends on them

## Files

- `rag_qna.ipynb` — main notebook
- `hp1.pdf` — source PDF
- `Book1.txt` — leftover text sample (optional)
- `README.md` — this file
