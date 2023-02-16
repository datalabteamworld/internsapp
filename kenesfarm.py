import streamlit as st

st.header("Kene's farm")
st.write("Organic farm produce")

st.radio("What type of chicken do you want?", ["Old layers", "Agric", "Broilers"])

st.radio("What type of vegetable do you want?", ["Pumpkin", "Water leaf", "Bitter leaf", "Freshly plucked oha leaves"])


st.radio("What type of fresh meat do you want?", ["Turkey", "Chicken", "Goat", "Snail"]) 
 
x = st.number_input("How many crates of fesh egg do you want?", step=1)

y = st.number_input("How many bags of snail do you need?", step=1)
a = st.number_input("How many pieces of fresh fish?", step=1)
b = int(x+y+a)

if st.button("Total number of produce"):
    st.sidebar.write(z)
