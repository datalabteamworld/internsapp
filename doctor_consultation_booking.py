import streamlit as st
import pandas as pd
import datetime
from PIL import Image
from streamlit_option_menu import option_menu
from datetime import date, timedelta as dt


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

img = Image.open("logo.png")
today = date.today()
default_appointment_date = today + dt(days=1)
default_appointment_time = today
default_apointment = today + dt(days=1)
min_dob = today - dt(days=36525)
st.sidebar.image(img,width=100)



def formattext(text):
    #this function format text into array to allow to count len of the text
    result = ', '.join(map(str, text))
    return result

def formattitle(text):
    #this functions formats text to begin with capital letter
    result = text.title()
    return result

def checkfieldExist(text):
    formattedtext = formattext(text)
    if len(formattedtext)  < 1:
        return ""
    else :
        return text
    
def calAge(birthdate):
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


    
    

with st.sidebar:
    st.title("Doctor Consultation BooKing")   
    selected = option_menu(
    menu_title = "",
    options = ["Consultation Form","View Booked Consultation", "About Us"],
    icons = ["pencil", "envelope","eye"],
     menu_icon="none",
    default_index = 0,
    
  )

styles = {st.container:{"background-color":"black"}
              }




if selected == "Consultation Form":
# formbtn = st.button("Form")

# if "formbtn_state" not in st.session_state:
#     st.session_state.formbtn_state = False

# if formbtn or st.session_state.formbtn_state:
#     st.session_state.formbtn_state = True
    st.title("Doctor's Consultation Form")
#     with st.form("my_form"):
    col1, col2,  = st.columns(2)
    with col1:
        st.markdown("**:blue[First name ]** ")
        firstname = st.text_input('First name', label_visibility="collapsed")
    with col2:
        st.markdown("**:blue[Last name ]** ")
        lastname = st.text_input('Last name', label_visibility="collapsed")
        
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**:blue[Date of Birth ]** ")
        dob = st.date_input('Date of Birth',  min_value=min_dob , max_value=today , label_visibility="collapsed")
    with col2:
        st.markdown("**:blue[Gender ]** ")
        gender = st.radio("Gender ",('Male', 'Female'), horizontal=True  , label_visibility="collapsed")
        
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**:blue[Email ]** ")
        email = st.text_input('Enter Email' , label_visibility="collapsed")
    with col2:
        st.markdown("**:blue[Phone Number ]** ")
        phone_number=st.text_input('Enter Phone Number' , label_visibility="collapsed")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**:blue[Do you have an account with us? ]** ")
        registration_status = st.radio("Do you have an account with us? ",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col2:
        st.markdown("**:blue[Hospital Registration Number]** ")
        registration_number = st.text_input('Enter Registration Number', label_visibility="collapsed")

    st.markdown("**:blue[Have you seen a doctor for the followings ?]** ")

    col1, col2 , col3 =st.columns([2,2,3])
    with col1:
        st.markdown("**:blue[High blood pressure ]** ")
    with col2:
        blood_pressure = st.radio("blood pressure",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col3:
        blood_pressure_note = st.text_input('blood_pressure_note' , label_visibility="collapsed", placeholder = "Type brief note here")

    col1, col2 , col3 = st.columns([2,2,3])
    with col1:
        st.markdown("**:blue[Heart disease ]** ")
    with col2:
        heart_disease = st.radio("heart disease",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col3:
        heart_disease_note =st.text_input('heart_disease_note' , label_visibility="collapsed", placeholder="Write a brief note")

    col1, col2 , col3 = st.columns([2,2,3])
    with col1:
        st.markdown("**:blue[High Cholesterol ]** ")
    with col2:
        cholesterol = st.radio("high cholesterol",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col3:
        cholesterol_note = st.text_input('cholesterol' , label_visibility="collapsed", placeholder="Write a brief note")

    col1, col2 , col3 = st.columns([2,2,3])
    with col1:
        st.markdown("**:blue[Diabetes ]** ")
    with col2:
        diabetes = st.radio("diabetes",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col3:
        diabetes_note = st.text_input('diabetes' , label_visibility="collapsed", placeholder="Write a brief note")

    col1, col2 , col3 = st.columns([2,2,3])
    with col1:
        st.markdown("**:blue[Bleeding disorder ]** ")
    with col2:
        bleeding_disorder = st.radio("bleeding_disorder",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col3:
        bleeding_disorder_note = st.text_input('bleeding_disorder' , label_visibility="collapsed", placeholder="Write a brief note")

    col1, col2 , col3 = st.columns([2,2,3])
    with col1:
        st.markdown("**:blue[Allergies ]** ")
    with col2:
        allergies = st.radio("allergies",('No', 'Yes'), horizontal=True , label_visibility="collapsed")
    with col3:
        allergies_note = st.text_input('allergies' , label_visibility="collapsed", placeholder="Write a brief note")

    st.markdown("**:blue[Please explain why do you want a consultation? ]** ")
    consultation_note = st.text_area('consultation' , label_visibility="collapsed", placeholder="Type here")

    st.markdown("**:blue[Have you undergone a surgery before? ]** ")
    surgery_status = st.radio("surgery status",('No', 'Yes'),  label_visibility="collapsed")

    st.markdown("**:blue[Please upload medical documents (if any)? ]** ")
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True , label_visibility="collapsed")
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
#         st.write("filename:", uploaded_file.name)
#         st.write(bytes_data)
   
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**:blue[Consultation Appointment Date ]** ")
        appointment_date = st.date_input("Desired Date of Appointment",  label_visibility="collapsed", min_value=today )
        
    with col2:
        st.markdown("**:blue[Select Appointment Time ]** ")
        appointment_time = st.selectbox('Who would you like to consult? ',('8:30 am','9:30 am', '10:30 am', '11:30 am' , '12:30 pm','2:30 pm', '3:30 pm') ,label_visibility="collapsed" )

    if 'appointment_time' not in st.session_state:
        st.session_state['appointment_time'] = appointment_time
    if 'appointment_date' not in st.session_state:
        st.session_state['appointment_date'] = appointment_date                                                                                  
    st.info(f"Your doctor's consultation will be {appointment_time} on  {date.strftime(appointment_date, '%A, %d %B %Y ')}")

    submitted = st.button("Submit")
    if submitted:
        error_message = []
        
        fname = formattext(firstname)
        lname = formattext(lastname)
        emailid = formattext(email)
        phone_num = formattext(phone_number)
                               
        if len(fname)  <= 1:
            message = "first name"
            error_message.append(message)
        if len(lname)  <= 1:
            message = "last name"
            error_message.append(message)
        if len(emailid) <= 1:
            message = "email"
            error_message.append(message)
        if len(phone_num) <= 1:
            message = "contact number"
            error_message.append(message)
        if registration_status == "Yes":
             if len(registration_number) <= 1:
                    message = "card number"
                    error_message.append(message)
                 
        if len(error_message) > 0:
              st.error(f"Kindly provide the following details to help us book your consultation: your {formattext(error_message)}")
          
               
        else:
                      
  
            if 'firstname' not in st.session_state or st.session_state['firstname'] != firstname:
                 st.session_state['firstname'] = firstname
            if 'lastname' not in st.session_state or st.session_state['lastname'] != lastname:
                 st.session_state['lastname'] = lastname
            if 'dob' not in st.session_state or st.session_state['dob'] != dob:
                 st.session_state['dob'] = dob
            if 'gender' not in st.session_state or st.session_state['gender'] != gender:
                 st.session_state['gender'] = gender 
            if 'email' not in st.session_state or st.session_state['email'] != email:
                 st.session_state['email'] = email
            if 'phone_number' not in st.session_state or st.session_state['phone_number'] != phone_number:
                 st.session_state['phone_number'] = phone_number
            if 'registration_status' not in st.session_state or st.session_state['registration_status'] != registration_status:
                 st.session_state['registration_status'] = registration_status
            if 'registration_number' not in st.session_state or st.session_state['registration_number'] != registration_number:
                 st.session_state['registration_number'] = registration_number
            if 'blood_pressure' not in st.session_state or st.session_state['blood_pressure'] != blood_pressure:
                 st.session_state['blood_pressure'] = blood_pressure
            if 'blood_pressure_note' not in st.session_state or st.session_state['blood_pressure_note'] != blood_pressure_note:
                 st.session_state['blood_pressure_note'] = blood_pressure_note
            if 'heart_disease' not in st.session_state or st.session_state['heart_disease'] != heart_disease:
                 st.session_state['heart_disease'] = heart_disease
            if 'heart_disease_note' not in st.session_state or st.session_state['heart_disease_note'] != heart_disease_note:
                 st.session_state['heart_disease_note'] = heart_disease_note
            if 'cholesterol' not in st.session_state or st.session_state['cholesterol'] != cholesterol:
                 st.session_state['cholesterol'] = cholesterol
            if 'cholesterol_note' not in st.session_state or st.session_state['cholesterol_note'] != cholesterol_note:
                 st.session_state['cholesterol_note'] = cholesterol_note
            if 'diabetes' not in st.session_state or st.session_state['diabetes'] != diabetes:
                 st.session_state['diabetes'] = diabetes
            if 'diabetes_note' not in st.session_state or st.session_state['diabetes_note'] != diabetes_note:
                 st.session_state['diabetes_note'] = diabetes_note
            if 'bleeding_disorder' not in st.session_state or st.session_state['bleeding_disorder'] != bleeding_disorder:
                 st.session_state['bleeding_disorder'] = bleeding_disorder
            if 'bleeding_disorder_note' not in st.session_state or st.session_state['bleeding_disorder_note'] != bleeding_disorder_note:
                 st.session_state['bleeding_disorder_note'] = bleeding_disorder_note
            if 'allergies' not in st.session_state or st.session_state['allergies'] != allergies:
                 st.session_state['allergies'] = allergies
            if 'allergies_note' not in st.session_state or st.session_state['allergies_note'] != allergies_note:
                 st.session_state['allergies_note'] = allergies_note
            if 'consultation_note' not in st.session_state or st.session_state['consultation_note'] != consultation_note:
                 st.session_state['consultation_note'] = consultation_note
            if 'surgery_status' not in st.session_state or st.session_state['surgery_status'] != surgery_status:
                 st.session_state['surgery_status'] = surgery_status
            if 'uploaded_files' not in st.session_state :
                 st.session_state['uploaded_files'] = uploaded_files
            if 'appointment_date' not in st.session_state or st.session_state['appointment_date'] != appointment_date:
                 st.session_state['appointment_date'] = appointment_date
            if 'appointment_time' not in st.session_state or st.session_state['appointment_time'] != appointment_time:
                 st.session_state['appointment_time'] = appointment_time
            if 'age' not in st.session_state or st.session_state['age'] != calAge(dob):
                 st.session_state['age'] = calAge(dob)
            
#             st.write(f"{dob} ({calAge(dob)} years old")   
            st.success(f"Hello {formattitle(firstname)} {formattitle(lastname)}, you appointment has been booked for {appointment_time} on  {date.strftime(appointment_date, '%A, %d %B %Y ')}. Select the View Appointment Menu to see more details")
            
            
       
    
if selected == "View Booked Consultation":
    st.title(f"{selected}")
    
   
    if 'firstname' not in st.session_state:
        st.warning("You have no booked doctor's consultation")
    
    else:
        name = formattitle(st.session_state.firstname) +" " + formattitle(st.session_state.lastname)
        birthdate = st.session_state['dob']
        formattedage = calAge(st.session_state['dob'])
     


        st.markdown("***:blue[Booked Consultation Details ]*** ")
        st.info(f"Your doctor's consultation will be {st.session_state.appointment_time} on  {date.strftime(st.session_state.appointment_date, '%A, %d %B %Y ')}")
       
        col1, col2,  = st.columns([2,4])
        with col1:
            st.markdown("**:blue[Names ]** ")
        with col2:
            st.write(name)
                
        col1, col2,  = st.columns([2,4])
        with col1:
             st.markdown("**:blue[Date of Birth / Gender  ]** ")
        with col2:
             st.write(f"{birthdate} ({formattedage} years old)  /  {st.session_state.gender}")
            
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[contacts (email / phone number)  ]** ")
        with col2:
              st.write(f"{st.session_state['email']}  /  {st.session_state['phone_number']}")
                
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Existing Patient status - Hospital Reg. Number ]** ")
        with col2:
              st.write(f"{st.session_state['registration_status']}  -  {st.session_state['registration_number']}")
                
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Blood Presure Status]** ")
        with col2:
              st.write(f"{st.session_state['blood_pressure']}  -  {st.session_state['blood_pressure_note']}")
         
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Heart Disease]** ")
        with col2:
              st.write(f"{st.session_state['heart_disease']}  -  {st.session_state['heart_disease_note']}")
                
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[High Cholesterol]** ")
        with col2:
              st.write(f"{st.session_state['cholesterol']}  -  {st.session_state['cholesterol_note']}")     
   
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Diabetes Status]** ")
        with col2:
              st.write(f"{st.session_state['diabetes']}  - {st.session_state['diabetes_note']}")
        
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Bleeding disorder]** ")
        with col2:
              st.write(f"{st.session_state['bleeding_disorder']}  -  {st.session_state['bleeding_disorder_note']}")

        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Allergies]** ")
        with col2:
              st.write(f"{st.session_state['allergies']}  -  {st.session_state['allergies_note']}")
         
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Surgery Status]** ")
        with col2:
              st.write(f"{st.session_state['surgery_status']} ")
        
        col1, col2,  = st.columns([2,4])
        with col1:
              st.markdown("**:blue[Consultation Description]** ")
        with col2:
              st.write(f"{ st.session_state['consultation_note']} ")

if selected == "About Us":
    st.title(f"{selected}")
    st.markdown("This platform helps patients book thier doctors consultation appointment online ")
   


   
   
          
                 
                 
                 
     
      
      
        
        