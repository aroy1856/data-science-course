# Assignment 32 - AI Agents (Tools + ReAct)

LangChain tools + tool-calling, then a `create_agent` ReAct-style agent that can search, calculate, check policy, and get date/time.

## How to run

1. open `agent.ipynb`
2. run top to bottom
3. `.env` needs `OPENAI_API_KEY` and `TAVILY_API_KEY` (for Tavily search)

needs: langchain, langchain-openai, langchain-community, langchain-tavily, python-dotenv

## What I did

**part 1 — tools**
- Tavily search + Wikipedia wrapper smoke tests
- custom `@tool calculator`
- conceptual notes: what tools are / chatbot vs agent

**part 2 — custom toolkit**
- `company_policy_lookup` (mock dict)
- `date_time_tool`
- toolkit list: policy + calculator + tavily + datetime

**part 3 — tool binding / calling**
- `llm.bind_tools(toolkit)`
- manual loop: HumanMessage → tool_calls → ToolMessage → final answer
- tested datetime + `2+(3*9)`

**part 4 — react agent**
- `create_agent(llm, tools, system_prompt=...)`
- invoke with `{"messages": [("user", "...)]}` (not old `{"input": ...}`)
- tests: capital of France, datetime, math, multi-step (Russia capital population, `(2+3)*9+7`)

**task 11 — insights**
- tool-agent benefits/challenges, chains vs agents, when agents beat plain RAG

## Where I struggled

- old ReAct string prompt as `system_prompt` + `invoke({"input": ...})` made the agent invent a datetime answer for “capital of France”
- fix: plain system prompt + `messages` invoke; let native tool-calling do the loop
- tool docs/arg schemas matter a lot — vague descriptions → wrong tool picks
- Tavily needs its own API key in `.env`

## Files

- `agent.ipynb` — notebook
- `README.md` — this file
