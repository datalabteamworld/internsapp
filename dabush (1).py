import streamlit as st
st.header("Dabush Hair Empire")
st.write(" we are your number one beauty salon for top notch beauty services")
st.write( "our services include \n making of attachment braids,\n relaxing of  hair of any texture,\n manicure \n pedicure\n makeup, gele tieing \n sales of hair extension ,\n sales of hair assesories,beauty products, home service delivery,treatment of damaged hair, hair  colouring, dredlocks")

with st.form(" clear_on_submit=false"):
    name = st.text_input ("name of the client")
    
    date = st.date_input(" appionmnet date")
    time = st.text_input(" time of the date")
    
    service = st.text_input(" what type of service do you need")
    
    complete = st.form_submit_button("submit")
   
if complete:
    st.write(name)
st.write("how satisfied are you with our services")

if st.button("satisfied"):
    st.write("good job") 
             
if st.button("nsatisfied"):
    st.write("unhappy customer")
st.write("names of available staff on duty")
st.text_input("olamide available on mondays")
st.text_input(" olabanji available on tuesdays")
st.text_input(" available all days of the week")
st.text_input(" available on weekends only")
    

                

   
    
    
    
   
