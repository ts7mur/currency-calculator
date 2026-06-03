import streamlit as st
from functions import get_all_currencies, convert_currency, calculate_profit


st.title("Currency and Profit Calculator")

currencies = get_all_currencies()


st.header("Currency Converter")

amount = st.number_input("Amount", value=100.0)

from_currency = st.selectbox(
    "From Currency",
    currencies,
    index=currencies.index("USD") if "USD" in currencies else 0
)

to_currency = st.selectbox(
    "To Currency",
    currencies,
    index=currencies.index("AED") if "AED" in currencies else 0
)

if st.button("Convert"):
    result = convert_currency(amount, from_currency, to_currency)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success(
            f'{result["amount"]} {result["from_currency"]} = '
            f'{result["converted_amount"]} {result["to_currency"]}'
        )

        st.write("Exchange rate:", result["exchange_rate"])


st.header("Profit Calculator")

cost = st.number_input("Cost", value=60.0)
selling_price = st.number_input("Selling Price", value=100.0)
target_margin = st.number_input("Target Margin %", value=40.0)

if st.button("Calculate Profit"):
    result = calculate_profit(cost, selling_price, target_margin)

    if "error" in result:
        st.error(result["error"])
    else:
        st.write("Profit:", result["profit"])
        st.write("Margin %:", result["margin_percent"])
        st.write("Markup %:", result["markup_percent"])
        st.write("Price needed for target margin:", result["price_for_target_margin"])