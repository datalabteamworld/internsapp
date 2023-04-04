import streamlit as st
from datetime import datetime
from PIL import Image
img =Image.open('NEW1.jpg')
new_image = img.resize((800,400))
st.image(new_image)

st.title("Welcome to Hephzibah Cleaning Services")

st.write('We render cleaning services to fooster your day to day activities')

st.sidebar.write ("please fill the required information")

st.sidebar.text_input('Enter your First Name')
         
st.sidebar.text_input('Enter your Last Name')

st.sidebar.text_input('Enter your Email Address')
                
st.sidebar.text_input('Enter your Mobile Number')
                    
st.sidebar.text_input('Enter your Service Location Address')   

st.selectbox ("Service Category",["Individual","Private Organisation", "Government Organisation"])
st.radio ("Service Type",["Contract","Monthly"])
NC=st.slider ("Number of Cleaners",0, 10)
DC=st.date_input ("Date of Commencement")

if st.button ("Payment Fees"):
    st.write(f"You are yet to pay")
        
if st.button ("Submit"):
    st.write(f"Your request have been submitted")
    st.write(f"Number of Cleaners: {NC}")
    st.write(f"Date of Commencement: {DC}")