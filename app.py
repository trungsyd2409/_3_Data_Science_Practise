import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("FX Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies is None:
    st.error("Error fetching currency list")

# Add input fields for capturing amount, from and to currencies
amount = st.number_input("Amount", value=1.0)
from_currency = st.selectbox("From Currency", options=currencies)
to_currency = st.selectbox("To Currency", options=currencies)

# Add a button to get and display the latest rate for selected currencies and amount
if st.button("Get Latest Rate"):
    if from_currency == to_currency:
        st.warning("Please select different currencies for conversion.")
    else:
        date, rate = get_latest_rates(from_currency, to_currency, amount)
        if rate is not None:
            st.success(format_output(
                date, from_currency, to_currency, rate, amount))
        else:
            st.error("Error fetching latest rate")

# Add a date selector (calendar)
date = st.date_input("Select Date", value=datetime.date.today(
), min_value=datetime.date(1999, 1, 4), max_value=datetime.date.today())

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button("Get Historical Rate"):
    if from_currency == to_currency:
        st.warning("Please select different currencies for conversion.")
    else:
        historical_rate = get_historical_rate(
            from_currency, to_currency, date, amount)
        if historical_rate is not None:
            st.success(format_output(date.strftime("%Y-%m-%d"),
                                     from_currency, to_currency, historical_rate, amount))
        else:
            st.error("Error fetching historical rate")
