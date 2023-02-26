import streamlit as st
import yfinance as fn
import pandas as pd

st.title("Streamlit Finance Dashboard")
tickers = ("PYPL", "MSFT", "FISV", "BTC-USD")

dropdown = st.multiselect("pick your assets", tickers)

start= st.date_input("Start", value = pd.to_datetime("2023-02-02"))
end = st.date_input("End", value = pd.to_datetime("today"))

if len(dropdown) > 0:
    df = fn.download(dropdown,start,end)['Adj Close']
    st.line_chart(df)
    