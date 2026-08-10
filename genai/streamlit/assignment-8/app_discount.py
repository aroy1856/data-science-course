import streamlit as st

st.title("Discount Calculator")
product_price = st.number_input(
    "Enter the product price:", 
    min_value=0, 
    step=1
    )

# Takes discount percentage (slider from 0 to 50%)  
discount_percentage = st.slider(
    "Enter the discount percentage:",
    min_value=0,
    max_value=50,
    step=1
    )

# Shows result using st.success()
if st.button("Calculate Discount"):
    discounted_price = product_price * (1 - discount_percentage / 100)
    st.success(f"Original Price: {product_price:.2f} \n Discount: {discount_percentage:.2f}% \n Final Price: {discounted_price:.2f}")