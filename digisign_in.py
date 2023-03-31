import streamlit as st
from datetime import datetime, date

st.title("DIGITAL SIGN IN")

st.write("How are you doing today?")
today = date.today()

st.text_input("WHAT IS YOUR NAME?")

st.sidebar.date_input("DATE")
st.sidebar.time_input("TIME IN")
st.selectbox("WHAT IS YOUR GENDER?", ["MALE","FEMALE"])
st.selectbox("SELECT WHICH APPLIES TO YOU",["STAFF","VISITOR"])
st.text_input("ENTER VISITOR'S PHONE NUMBER")

st.sidebar.time_input("TIME OUT")
st.text_input("ENTER STAFF ID NUMBER")
st.text_input("ENTER LAPTOP SERIAL NUMBER")


st.button("submit")
    
