# Assignment 33 - Chat with SQL (Text-to-SQL Agent)

SQLite `company.db` + LangChain SQL toolkit/agent. ask English questions, agent writes SQL. optional MySQL Workbench via `MYSQL_URI`.

## How to run

1. open `text2sql.ipynb`
2. run top to bottom (creates `company.db` in this folder)
3. `.env` needs `OPENAI_API_KEY`

**optional MySQL Workbench**
```env
MYSQL_URI=mysql+pymysql://user:pass@127.0.0.1:3306/company
```
also: `uv add pymysql` and keep Workbench/MySQL running. if URI missing, notebook skips MySQL and still demos SQLite.

needs: langchain, langchain-openai, langchain-community, sqlalchemy, python-dotenv

## What I did

**part 1 — sqlite**
- created `company.db` with `employees` + `sales`
- inserted 11 employees / 12 sales rows
- verified with COUNT + sample SELECTs

**part 2 — langchain db**
- SQLAlchemy engine → list tables
- `SQLDatabase.from_uri("sqlite:///company.db")` + schema print

**part 3 — mysql workbench**
- connect code via `MYSQL_URI` (skips cleanly if not set / server down)

**part 4 — sql toolkit + agent**
- `SQLDatabaseToolkit` tools (list tables / schema / query / checker)
- `create_agent(...)` with read-only-ish system prompt
- `ask_sql(question, backend="sqlite"|"mysql")`
- asked: employees per dept, highest salary, total sales, avg salary / dept

**safety + insights**
- ambiguous qs (“best employee”, “show numbers”) + refused destructive vibe (“delete all”)
- writeup: SQL agent vs hand SQL, vs RAG, risks of open SQL access

## Where I struggled

- modern agent wants `{"messages": [("user", "...)]}` not old `{"input": ...}`
- MySQL needs Workbench/server + `pymysql` + URI — easy to skip locally, so made it optional
- agent sometimes over-explains; keep temperature=0 and a short system prompt
- dont give the agent write access on real DBs

## Files

- `text2sql.ipynb` — notebook
- `company.db` — created when you run the notebook
- `README.md` — this file
