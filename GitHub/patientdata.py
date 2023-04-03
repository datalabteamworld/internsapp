import streamlit as st
st.title ("Excellent Hospital Patient Data Entry app")
st.text_input("Patient name")
st. number_input("Patient age")
st.selectbox("Patient gender",["Male","Female"])
 
st.write("if Female, enter L.M.P")
st.text_input("enter date")
                       
w= st.sidebar.number_input("patient weight in kg", step=0.1)
h= st.sidebar.number_input("patient height in meters", step=0.1)
                       
if st.button("Calculate"):
                        
                        def bmi(name, height_m, weight_kg):bmi = w/(h*h)
                        bmi = round(bmi,2)                     
                        if bmi >25: st.write("overweight") 
                        elif 18.4 < bmi < 25.1: st.write("Normal")
else:st.write("underweight")
                                 
                                 
st.sidebar.number_input("Body tempreature")
st.sidebar.number_input("Patient B.P")
                                 
                                 
                                 
st.text_input('Date of First appointment')

st.selectbox("Does patient have any chronic ailment?", ["Yes","No"])
   
st.selectbox("Appointment type",["First Visit", "Routine checkup", "Antenatal"])
                                               
                                               
st.text_input("Next appointment Date")
