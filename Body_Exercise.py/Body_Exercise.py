import streamlit as st

st.header("KEEPFIT TRANSFORMATION CHALLENGE APPLICATION")

st.write("In order to help you do Aerobics exercise in a much simpler way.")
st.write("So let's get started.")
from PIL import Image
open_img = Image.open("exe2.jpg") 
st.sidebar.image(open_img, width=600)

st. subheader("Personal Details")

st.write("Name;")
st.text_input("First name")
st.text_input("Last name")

col1, col2 = st.columns ([1,2])
with col1:
    st.number_input("Age", step = 1)
with col2:
    gender = st.radio("Gender", ["Male","Female"])
    st.success(gender)


st.write("Address;")
st.text_input("Home Address")

col1, col2, col3, col4 = st.columns ([1,2,3,4])
with col1:
    st.text_input("City")
with col2:
    st.text_input("State/province")
with col3:
    st.text_input("Postal/Zip code")
with col4:
    st.text_input("Country")
    

st.write("Phone number;")
col1, col2 = st.columns ([1,2])
with col1:
    st.text_input("Area code")
with col2:
    st.text_input("Phone Number")

st.text_input("Email;")

st.write("Medical info;")

st.text_input("Any medical issue we need to know about?")

col1,col2 = st.columns([1,2])
with col1:
    st.text_input("Emergency contact person")
with col2:
    st.text_input("Relationship")


st.write("Lets answer a few question so that we can help you better:")

activity = st.radio("What does your typical day looks like?", ["sitting all day", "Standing all day", "A little physical activity", "Others"])
st.success(activity)

diet = st.radio("What's your diet type?", ["Standard ; All kinds of food", "Vegetarian ; Meat-free or Fish-    free"])
st.success(diet)

eat = st.radio("Do you eat around the same time everyday", ["Yes", "No"])
st.success(eat)

body = st.radio("Whats your focus part?", ["Full body", "Arm","Abs", "Butt", "Leg"])
st.success(body)


st.markdown("We can help you! Get better result with professional guidance. Let's start personalizing your plan.")

st.subheader("Calculate your BMI")
w = st.number_input("Weight in Kg", step = 0.1)
h = st.number_input("Height in meters", step = 0.1)

if st.button("Calculate"):
    bmi = w/(h*h)
    bmi = round(bmi,2)
    if bmi > 25:
        st.warning(f"Your BMI is {bmi}, click Challenge, you need to shed some weight.")
    elif 18.5 < bmi < 25:
        st.success(f"Your BMI is {bmi}, click Easy, contiune to keep fit.")
    else:
        st.error(f"Your BMI is {bmi}, click Easy, feed well as you keep fit.")
        
st.number_input("What is your target weight? ")
level = st.slider("How fast do you want to reach your goal? ", 0,10 )
st.text('Selected: {}'.format(level))
st.text_input("Why do you want to join the KEEPFIT FITNESS GROUP?")

st.markdown("Always do your workout from easy to challenge.")
st.markdown("Have a fun daily workout.")
st.markdown("I realize that my answers to the above questions will be considered by KEEPFIT FITNESS GROUP in determining whether I shall be permitted to participate in certain programs offered.  I certify that my answers are true and correct and in the event that any answers should prove to be untrue, I release KEEPFIT FITNESS GROUP from any and all liability, loss cost, damage and expenses resulting from its reliance thereof.")

st.checkbox("I have Read Understand and Agree to the KEEPFIT TRANSFORMATION CHALLENGE Rules and Regulations")
st.button("Submit")
