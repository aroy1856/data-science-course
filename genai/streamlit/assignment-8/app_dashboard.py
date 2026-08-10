import streamlit as st

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

st.title("Simple Sales Dashboard")
st.write("Sales data by month:")

months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month:", months)
st.metric(f"Sales for {selected_month}:", sales[selected_month])
st.bar_chart(sales)