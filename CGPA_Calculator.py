import streamlit as st
from PIL import Image

img = Image.open('images.jpeg') 
st.sidebar.image(img)

st.title("My CGPA Calculator")

qp = st.number_input("what is your total quality point")
cu = st.number_input("what is your total credit unit")


if st.button("Calculate"):
    cgpa = qp/cu
    cgpa = round(cgpa,2)
    
    if cgpa > 4.44:
        st.write(f'your CGPA is {cgpa}, First Class Honours\n Excellent result')
    elif 3.59 < cgpa < 4.45:
        st.write(f'your CGPA is {cgpa}, Upper Second Class Honours\n Very good result')
    elif 2.99 < cgpa < 4:
        st.write(f'your CGPA is {cgpa}, Lower Second Class Honours\n good result')
    elif 2.49 < cgpa < 3:
        st.write(f'your CGPA is {cgpa}, Third Class Honours\n You need to improve')
    elif 1.9 < cgpa < 2.5:
        st.write(f'your CGPA is {cgpa}, Pass\n Very poor result')
    elif cgpa > 1:
        st.write(f'your CGPA is {cgpa}\n You cannot graduate')
                 
    
        

                 
