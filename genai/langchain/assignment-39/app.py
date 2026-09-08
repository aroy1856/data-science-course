import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import ast
import operator as op

# load .env from cwd or parents
for p in [Path.cwd(), *Path.cwd().parents]:
    if (p / ".env").exists():
        load_dotenv(p / ".env", override=True)
        break

if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY is not set in .env")
    st.stop()

st.set_page_config(page_title="Text-to-Math Agent", page_icon="🧮")
st.title("Text-to-Math Agent")
st.caption("Word problems → steps → calculator tool → answer. History kept in session_state.")

_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.Mod: op.mod,
}


def _eval_node(node):
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.operand))
    raise ValueError(f"unsupported expression: {ast.dump(node)}")


@tool
def calculator(expression: str) -> float:
    """Evaluate a math expression like '2+(3*9)' or '800*0.8'. Use for exact arithmetic."""
    tree = ast.parse(expression.replace("^", "**"), mode="eval")
    return float(_eval_node(tree))


@st.cache_resource
def get_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    system_prompt = """You are a Text-to-Math agent.
Read the word problem, break it into steps, and use the calculator tool for exact math.
Use prior chat turns as context when the user asks follow-ups.
Give a short Final Answer.
"""
    return create_agent(llm, tools=[calculator], system_prompt=system_prompt)


agent = get_agent()

# --- session state: conversation history ---
if "messages" not in st.session_state:
    st.session_state.messages = []  # list[{"role","content"}]

# show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask a math word problem...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # pass full history so follow-ups keep math context
    history_msgs = [(m["role"], m["content"]) for m in st.session_state.messages]
    with st.chat_message("assistant"):
        with st.spinner("Calculating..."):
            result = agent.invoke({"messages": history_msgs})
            answer = result["messages"][-1].content
            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

with st.sidebar:
    st.subheader("Session")
    st.write(f"Turns stored: {len(st.session_state.messages)}")
    if st.button("Clear chat history"):
        st.session_state.messages = []
        st.rerun()
