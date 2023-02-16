
import streamlit as st
from PIL import Image

img = Image.open("HI.jpeg")
st.sidebar.image(img)


st.header("Nice to have you in my First App")
st.write("This App will WHAO you")

st.write("Your Success is My Joy")

a = st.text_input('First name')
b = st.text_input('Surname', key = 1) 
c = st.text_input('Gender', key = 2) 
d = st.text_input('Position applied for', key = 3) 
e = st.number_input('How many Years of experience do you have', step = 1)
f = st.text_input('Expected salary')

if st.button('submit'):


    if e < 10:
        st.write('NOT QUALIFIED')   
    else:
        st.write('QUALIFIED')









