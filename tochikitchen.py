import streamlit as st

st.header("Tochi's kitchen")
st.write("A meal made in a home far away from home")

st.radio("What type of soup do you want?", ["Okro", "Oha", "Egwusi", "Ogbono", "Nsala"])

st.radio("What type of swallow do you want?", ["Fufu", "Semovita", "Pounded yam"])

st.radio("What type of rice do you want?", ["Coconut", "Jollof", "Fried", "Native"]) 

st.radio("What type of meat do you want?", ["Turkey", "Beef", "Chicken", "Goat", "Snail"]) 
st.radio("How do you want your meat?", ["Spicy", "Grilled", "Fried", "Tender", "Boiled"]) 

t = st.sidebar.number_input("How many plates of soup do you need?", step=1)

x = st.sidebar.number_input("How many pieces of swallow do you want?", step=1)

y = st.sidebar.number_input("How many plates of rice do you need?", step=1)
a = st.sidebar.number_input("How many plates of meat do you need?", step=1)


z = int(t+x+y+a)

if st.sidebar.button("Total"):
    st.sidebar.write(z)
    
st.sidebar.selectbox("Method of delivery", ["pickup", "home delivery"])

st. sidebar.write("PAYMENT VALIDATES ORDER")
st.sidebar.checkbox( "Transfer Only")