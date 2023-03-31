import streamlit as st
from PIL import Image

st.sidebar.header("Staff Booking Service")
pic = Image.open("food.jpeg")
new_pic = pic.resize((300,200))
st.sidebar.image(new_pic)

pic1 = Image.open("logo.jpg")
new_pic1 = pic1.resize((50,50))
st.image(new_pic1)
with st.sidebar.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Kitchen I.D")
    st.form_submit_button("Login")

st.header("Welcome to Supreme Kitchen")
st.subheader("The Oasis of finger licking meals...")

img = Image.open("Serve.jpeg")
new_img = img.resize((400, 200))
st.image(new_img)

st.write("Book your finger licking meals below.")

st.radio("Select your serving option", ["Eat in", "Take away"])

st.write("Monday")
st.selectbox("Select meal", ["Fried rice", "Rice and stew", "Jollof rice"])
st.write("Tuesday")
st.selectbox("Select meal", ["Spaghetti pepperoni", "Spaghetti bolognese", "Jollof spaghetti"])
st.write("Wednesday")
st.selectbox("Select meal", ["Yam porridge with vegetables", "Sweet potato with fish sauce", "Irish potato with chicken sauce"])
st.write("Thursday")
st.selectbox("Select meal", ["Beans with fried plantain", "Beans with potato chips", "Beans with bread"])
st.write("Friday")
st.selectbox("Select meal", ["Eba and okro", "Amala and ewedu", "Semo and Egusi"])

st.number_input("Select number of portions", step = 1)

st.checkbox("I want appetizers")
st.checkbox("I want desserts")

st.radio("Select fluid (optional)", ["Water", "Fruit Juice", "Soft drink"])
st.slider("Rate your satisfaction from last week's meals.",0,10)
st.text_input("Type your feedback to help us serve you better.")

st.subheader("We are so grateful for the pleasure of serving you!")
img1 = Image.open("thank.jpg")
new_img1 = img1.resize((400, 200))
st.image(new_img1)