"""Streamlit CodeLlama assistant (Ollama)."""

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

MODEL = "codellama:7b"

PROMPTS = {
    "Generate Code": ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a senior software engineer. Generate clean, working code.\n"
                "Rules:\n"
                "- Prefer Python unless another language is requested\n"
                "- Include a short docstring\n"
                "- Output only the code in a fenced markdown block, then 2–4 bullet notes",
            ),
            ("human", "Generate code for:\n{input}"),
        ]
    ),
    "Explain Code": ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You explain code clearly for a junior developer.\n"
                "Structure your answer as:\n"
                "1. What it does (1–2 sentences)\n"
                "2. Step-by-step walkthrough\n"
                "3. Edge cases / caveats",
            ),
            ("human", "Explain this code:\n{input}"),
        ]
    ),
    "Debug Code": ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You debug broken code.\n"
                "Structure your answer as:\n"
                "1. Bug(s) found\n"
                "2. Why it fails\n"
                "3. Fixed code in a fenced markdown block",
            ),
            ("human", "Find and fix bugs in this code:\n{input}"),
        ]
    ),
    "Optimize Code": ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You suggest practical optimizations.\n"
                "Structure your answer as:\n"
                "1. Bottlenecks / smells\n"
                "2. Suggested improvements (bullets)\n"
                "3. Optimized code in a fenced markdown block",
            ),
            ("human", "Optimize this code:\n{input}"),
        ]
    ),
}


@st.cache_resource
def get_llm():
    return ChatOllama(model=MODEL, temperature=0.1)


st.set_page_config(page_title="CodeLlama Assistant", page_icon="🦙")
st.title("CodeLlama Code Assistant")
st.caption(f"Local Ollama model: `{MODEL}` — generate / explain / debug / optimize")

task = st.selectbox("Task type", list(PROMPTS.keys()))
user_text = st.text_area(
    "Code or prompt",
    height=220,
    placeholder="Paste code, or describe what to generate…",
)

if st.button("Run CodeLlama", type="primary", disabled=not user_text.strip()):
    with st.spinner(f"Running {task} on {MODEL}…"):
        try:
            chain = PROMPTS[task] | get_llm() | StrOutputParser()
            output = chain.invoke({"input": user_text})
        except Exception as e:
            st.error(
                f"Ollama call failed. Is the daemon running and `{MODEL}` pulled?\n\n{e}"
            )
            st.stop()

    st.subheader("Output")
    st.markdown(output)
