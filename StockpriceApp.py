import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='Id', start='2012-5-31', end='2023-2-28')
# Open  High  Low Close  Volume  Dividends  Stock splits
 
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)