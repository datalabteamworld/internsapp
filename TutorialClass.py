import streamlit as st

st.header("TUTORIAL CLASS")
st.subheader("Maths Tutorial Class")

st.header("Personal Information")
st.text_input("First Name")
st.text_input("Last Name")
st.text_input("Parent/Guardian Name")
st.text_input("Parent/Guardian Phone Number")
st.radio("Gender", ["Male","Female"])

st.date_input("Date of Birth")
st.text_input("Phone Number")
st.text_input("Home Address")
st.text_input("State")

col1,col2,col3 = st.columns([1,2,3])
with col1:
    st.text_input("State")
                  
with col2:
    st.text_input("City")
    
with col3:
    st.text_input("Country")
    
st.subheader("Lesson Time")
st.selectbox("Sections", ["Morning : 9am - 11am", "Afernoon : 12am - 3am", "Evening : 3pm - 5pm"])

rate = st.slider("How fast can you understand Maths", 10, 100)
st.success("rate")

st.button("Submit")
    
    
    
    