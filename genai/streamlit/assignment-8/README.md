# GenAI Assignment 8 - Streamlit Basics

First proper Streamlit assignment — just getting comfortable with titles, inputs, buttons, sidebar forms, metrics, and a tiny bar chart. Four small apps, nothing with sessions / APIs / uploads / databases.

## How to run

From this folder (or the project root), pick whichever app you want:

```bash
streamlit run app_basic.py
streamlit run app_discount.py
streamlit run app_product_form.py
streamlit run app_dashboard.py
```

Needs `streamlit` installed.

## What's inside

**Task 1 - Basic greeting app (`app_basic.py`)**  
Title "Welcome to Streamlit!", a name text input, and a "Greet Me" button that prints `Hello, <name>!`. Pretty much just `st.title` / `st.text_input` / `st.button` / `st.write`.

**Task 2 - Discount calculator (`app_discount.py`)**  
Number input for price, slider for discount (0–50%), then on button click it shows original / discount / final price with `st.success()`.

**Task 3 - Product form (`app_product_form.py`)**  
Sidebar form: product name, category selectbox (a few options), and price. Hit "Add Product" and it shows a success message plus the details on the main page.

**Task 4 - Mini sales dashboard (`app_dashboard.py`)**  
"Simple Sales Dashboard" with a month selectbox, a tiny hardcoded sales dict, `st.metric` for the selected month, and `st.bar_chart` for all months. No pandas — just a plain dict.

## Files

- `app_basic.py` — greeting app
- `app_discount.py` — price / discount calculator
- `app_product_form.py` — sidebar product form
- `app_dashboard.py` — month sales dashboard
- `README.md` — this file
