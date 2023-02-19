import streamlit as st
st.header("Welcome to MyHealth Plux")
st.write("MyHealth Plux blood sugar calculation helps you convert your blood glucose reading from mmol to mg/dl and vice-versa")
st.write("Blood sugar monitoring helps to determine if you are meeting your glucose tagets which helps to reduce the unpleasant symptoms of high and low blood sugar and avoid long term diabetes complications")
st.sidebar.write("Let's Go!")
st.sidebar.title("Fasting Blood Sugar Calculator")
x=st.sidebar.number_input("what is your fasting blood sugar?mmol/l ")
x1=int((x)*18)
if st.sidebar.button("Result"):
    st.sidebar.write(f"Your fasting blood Sugar is {x1}mg/dl")
x1=round(x1,1)
if x1<100:
    st.sidebar.write(f"Normal")
elif x1==100:
    st.sidebar.write(f"Normal")
elif 100>=126:
    st.sidebar.write(f"You are at risk of diabetes")
else:
    st.sidebar.write("Diabetic,please see your doctor")
st.sidebar.title("Random Blood Sugar Calculator")
y=st.sidebar.number_input("what is your Random blood sugar?mmol/l ")
y1=int((y)*18)
if st.sidebar.button("Calculate"):
    st.sidebar.write(f"Your Random blood Sugar is {y1}mg/dl")
y1=round(y1,1)
if y1<200:
    st.sidebar.write(f"Normal")
elif y1==200:
    st.sidebar.write(f"Normal")
else:
    st.sidebar.write("Diabetic,please see your doctor")
import streamlit as st
from PIL import Image
image=Image.open("newb.jpeg")
st.image(image,caption="Glucometer")