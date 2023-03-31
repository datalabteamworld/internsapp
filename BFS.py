
import streamlit as st
from PIL import Image

img1 = Image.open('BFS ANIMATION.gif')
st.sidebar.image(img1, width=300)

img2 = Image.open('bfs starch .jpg')
st.sidebar.image(img2, width=300)



st.header("WELCOME TO BFS GLOBAL ENTERPRISE")

st.write("motto: your satisfaction is our pride")

st.write("PLACE YOUR ORDER AND IT SHALL BE DELIVERED AT YOU DOOR STEP")
st.write("select from the beside product")
st.write("picture 1 is 5l cold water starch which cost #3500")
st.write("picture 2 consist of 1l cold water starch and our spray starch")
st.write("1l cold water starch cost #1000")
st.write("spray starch cost #850")

x =st.number_input("input your first selected product price") 

y =st.number_input("input your second selected product price")

w =st.number_input("input your third selected product price") 


z= int(x+y+w)

if st.button("add"):
    st.write(f'the total price is #{z}')
    
    if z > 0:
        st.write(f'we really apreciate you patronage, God bless you')
        
st.radio("are you a first time customer", ["Yes", "No"])

with st.form(key='my_form'):
    address = st.text_input('delivery address')
    phonenumber = st.text_input('phone number')
    st.form_submit_button('submit')
    
    
        