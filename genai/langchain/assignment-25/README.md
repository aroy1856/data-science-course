# Assignment 25 - Prompts, Chains & LCEL

LangChain prompts → structured Pydantic output → simple / conditional / parallel chains → LCEL RAG pipeline.

## How to run

1. open `chain.ipynb`
2. run top to bottom
3. put `OPENAI_API_KEY` in the repo `.env`

needs: langchain-openai, langchain-community, langchain-text-splitters, chromadb / chroma, pydantic, python-dotenv

## What I did

**part 1 — prompts**
- `PromptTemplate` with `{question}`, tested a few topics
- `ChatPromptTemplate` with System / Human / AI messages (format → `llm.invoke(messages)`)

**part 2 — structured output**
- Pydantic `Answer(answer, confidence, source)` + `PydanticOutputParser`
- chain: `prompt | llm | parser`
- try/except fallback when parsing fails

**part 3 — chains**
- simple LCEL: `prompt | llm | StrOutputParser`
- chroma retriever over transformer notes + RAG-style chain
- conditional: `RunnableBranch` — factual keywords → retriever, else direct LLM
- parallel: answer + summary + follow-ups via `RunnableParallel`

**part 4 — runnables / LCEL RAG**
- `|` composition + `RunnablePassthrough` for string queries
- tested multiple transformer questions against the vector store

**task 10 — insights**
- why structured output, LCEL vs old chains, parallel vs conditional

## Where I struggled

- `llm.invoke(ChatPromptTemplate)` fails — need `prompt.format_messages()` (or `prompt | llm`) first
- retriever got a dict and blew up (`TypeError: 'dict' object is not an instance of 'str'`) — pass a string query, or `itemgetter("question")` before the retriever
- chroma chunk warnings when text chunks > `chunk_size`

## Files

- `chain.ipynb` — main notebook
- `chroma_db/` — persisted Chroma store from the notebook
- `README.md` — this file
