import streamlit as st

st.title("Welcome to Fadeke Fertility Center")
st.subheader("Virtual consultations are available. Please call or fill out the form below to request a new patient appointment. A member of our new patient center will call you to schedule an appointment.")
st.write("To schedule new patient appointment, fill out the form below")

st.header("New Patient Appointment")

st.camera_input("Take a Picture of yourself, Please note that this needed to capture your current look")


col1, col2 = st.columns(2)
col1=st.text_area("First Name",)
col2=st.text_area("Last Name",)

col3, = st.columns(1)
col3=st.text_area("City")
st.selectbox('State', ['Kwara','Lagos','Osun','Oyo','Ogun','Ekiti','Edo',])

col5, col6 = st.columns(2)
col5=st.text_area("Date of birth, DD/MM/YYYY")
col6=st.text_area("Email Address")

col7, col8 = st.columns(2)
col7=st.text_area("Phone Number")
col8=st.text_area("Insurance Company")

st.write("What time would you love to see the Doctor")
st.selectbox('What Time would you like to see the doctor', ['7 am', '7:45am', '8:00am','8:45am','9:00am','9:45am','10:00am','10:45am'])

st.selectbox('How did you hear about us', ['Friend or Patient', 'Online', 'Insurance','Radio or Streaming','Seminar of Webinar','Fertility or Donor Agencies','TV or Print','Self'])

st.text_area("If refferd by a physician, please supply name")

st.radio('I would like to start receiving email communication from Fadeke Fertility Centre',['Yes', 'No'])


st.button("Submit")



