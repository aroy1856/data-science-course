# Assignment 27 - Message History / Chat Memory

LangChain multi-turn chat: message types, `MessagesPlaceholder`, in-memory history, trimming, then a small Q&A chatbot that remembers follow-ups.

## How to run

1. open `message_history.ipynb`
2. run top to bottom
3. put `OPENAI_API_KEY` in repo `.env`

needs: langchain-openai, langchain-core, python-dotenv

## What I did

**task 1 — message concepts**
- System / Human / AI messages = roles in a chat transcript
- message lists beat one big string prompt for multi-turn

**task 2 — MessagesPlaceholder**
- `ChatPromptTemplate` with `MessagesPlaceholder("chat_history")`
- `RunnableWithMessageHistory` + `InMemoryChatMessageHistory` keyed by `session_id`
- tested: name remember + book suggestion follow-ups (`abhi1`)

**task 3 — basic history**
- same pattern, new session (`abhi2`) — store appends turns automatically via the runnable

**task 4 — trimming**
- simple `trim_by_count()` (last N messages)
- `trim_messages(max_tokens=..., strategy="last")` for token budget

**task 5–6 — Q&A chatbot**
- history + token trimmer wired with `RunnablePassthrough.assign`
- follow-ups: python lists → example → tuples
- stateful demo: Transformer → vs RNN → “what is the future?”

**task 7 — insights**
- why history matters, long-memory tradeoffs, trim vs summarize, placeholder vs memory store

## Where I struggled

- `RunnableWithMessageHistory` shows a deprecation warning (LangGraph persistence is the new path) — still fine for this assignment
- forgetting `config={'configurable': {'session_id': ...}}` = no history / new empty session every time
- trimmer needs the history list *before* the prompt — used `RunnablePassthrough.assign(chat_history=...)`
- token trim counts depend on `token_counter=llm`, so limits are approximate

## Files

- `message_history.ipynb` — main notebook
- `README.md` — this file
