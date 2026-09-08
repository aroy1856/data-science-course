# Assignment 35 - Text-to-Math Agent

Word-problem math agent: LLM plans steps, `calculator` tool does exact arithmetic. Notebook + Streamlit chat with `session_state` history.

## How to run

**Notebook**
1. open `text2Math.ipynb`
2. run top to bottom
3. put `OPENAI_API_KEY` in repo `.env`

**Streamlit app**
```bash
cd genai/langchain/assignment-35
streamlit run app.py
```

needs: langchain, langchain-openai, streamlit, python-dotenv

## What I did

**task 1 — concepts**
- text-to-math = NL word problem needing calc
- agents useful because they can call a calculator instead of guessing
- plain LLM vs agent: one-shot guess vs tool-using steps

**task 2 — agent**
- safe-ish `@tool calculator` (AST eval, no raw `eval`)
- `create_agent(gpt-4o-mini, tools=[calculator], system_prompt=...)`
- invoke with `{"messages": [("user", "...)]}`
- tested:
  - notebooks+pens total cost
  - 20% off on 800
  - solve `2x+5=17`

**task 3 — streamlit session state**
- `app.py` chat UI
- `st.session_state.messages` stores Q&A turns
- full history passed back into the agent so follow-ups keep math context
- sidebar clear-history button

## Where I struggled

- dont use old ReAct string templates / `{"input": ...}` with modern `create_agent`
- Streamlit reruns wipe locals — history *must* live in `session_state`
- LLM still needs a good prompt telling it to use the calculator for exact numbers

## Files

- `text2Math.ipynb` — notebook
- `app.py` — Streamlit chat app
- `README.md` — this file
