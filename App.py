import streamlit as st
from PIL import Image

#sidebar
st.sidebar.header("ALGORITHM COLLEGE")
img = Image.open('logo.png')
st.sidebar.image(img)

st.sidebar.write("At Algorithm College, we help you kickstart your career irrespective of your age, gender or nationality.")

#main
st.header("STUDENTS BIODATA APP")
name = st.text_input("FIRST NAME")
st.text_input("LAST NAME")

if st.button("Click here to add your Age"):
    st.write("Ooops!, Age is just a number, anyone can learn how to code irrespective of age, gender or nationality")
    
st.text_input("E-MAIL")
st.text_input("PHONE NUMBER")
st.radio("GENDER", ["Male","Female"])

st.selectbox("PREFERRED TECH CAREER",["Data Science", "Web Design", "Graphic Design", "Data Analytics"])
st.multiselect("PREFERRED PROGRAMMING LANGUAGE(S)",["Python","Java","SQL","C++"])

st.selectbox("How did you find out about Algorithm College ?",["Facebook", "Instagram", "Twitter", "LinkedIn","Google Search", "Through a friend"])

if st.button("Submit"):
    st.write(f" {name}, Welcome to Algorithm College ")
