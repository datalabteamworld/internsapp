import streamlit as st

from PIL import Image
img = Image.open("pix.png")
st.sidebar.image(img)
st.sidebar.text_input("What is your name?")

st.sidebar.number_input("Membership number", step = 1)

st.header("LEENAS SAVINGS COOPERATIVE")

st.subheader("WELCOME")

x = st.number_input("Enter amount", step = 1)
y = st. number_input ("Days of savings", step = 1)


if st.button("calculate"):
    z = int(x*y)

    st.write(f"Your total savings is {z}")