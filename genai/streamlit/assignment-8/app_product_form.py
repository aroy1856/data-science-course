import streamlit as st

st.sidebar.title("Product Form")
st.sidebar.write("Please enter the product details:")

product_name = st.sidebar.text_input("Product Name")
product_category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Books", "Furniture", "Other"])
product_price = st.sidebar.number_input("Price", min_value=0, step=1)

if st.sidebar.button("Add Product"):
    st.success(f"Product added successfully")
    st.write(f"Product: {product_name} \n Category: {product_category} \n Price: {product_price}")