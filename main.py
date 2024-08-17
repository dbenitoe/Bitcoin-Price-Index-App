import streamlit as st
from backend import fetch_bitcoin_prices as bp
from backend import calculate_price as calculate

# Add Title, text input, slider, selectbox, and subheader
st.title("Bitcoin Value Converter")
input_value = st.text_input("Enter the amount of Bitcoin you have: ")
option = st.selectbox("Select currency code", ("USD", "EUR", "GBP"))

# Check if the input is not empty and is a valid integer
if input_value:
    try:
        amount = float(input_value)
        prices = bp()

        if prices is None:
            st.error("Error fetching BitCoin price.")
        else:
            messages = calculate(prices,amount,option)
            st.write(messages[0])
            st.write(messages[1])
    except ValueError:
        st.error("Please enter a valid number.")
else:
    st.warning("Please enter an amount.")


