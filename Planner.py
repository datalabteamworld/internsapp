import streamlit as st
from PIL import Image

st.title ("Personalised Healthy Meal Planner")

Username = st.sidebar.text_input("Username")
Password = st.sidebar.text_input("Password")
st.sidebar.checkbox ("Keep me signed in")
col1, col2, =st.columns(2)
with col1:
    if st.sidebar.button("Login"):
        st.write ("Login")
st.sidebar.write("Not yet a user?")
with col2:
    if st.sidebar.button("Sign up"):
        st.write ("Sign up")
        
image = Image.open ('Capture.jpg')
new_image = image.resize ((2,1))
st.image(image)

st.selectbox("How long would you plan your meals for?", ["1-day-week","2-day-week", "3-day-week","4-day-week","5-day-week"])

meals= st.radio("Which meal would you like to include in your plan?",[ "Breakfast", "Lunch","Dinner"])

st.multiselect("Any do not include?", ["None","Dairy products","Eggs", "Seafood","Pork"])

if st.button("Create meal plan"):
    if meals == "Breakfast":
        st.write ("Let's make Salad.  \n You will need; ", {"Cabbage" ,"Eggs", "Chicken", "Cucumber", "Carrots", "Baked beans", "Salad cream"})
    elif meals== "Lunch":
        st.write ("Let's make Eforiro.   \n You will need;",{"Vegetable", "Semo", "Goat meat","Fish","Palm oil"})
    elif meals == "Dinner":
        st.write ("Let's make Joll of rice.   \n You will need;",{"Rice","Tomatoes", "Vegetables", "Fish"})
    else: st.write (" You have not made any meal selection")
    


    












   





    



