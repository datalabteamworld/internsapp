import streamlit as st

from PIL import Image

image = Image.open("hospital logo.jpg")
new_image1 = image.resize((200, 200))

image = Image.open("hospital picture.jpg")
new_image2 = image.resize((200, 200))

st.image([new_image1 ,new_image2])

image = Image.open("hospitalman.jpg")
new_image3 = image.resize((150, 150))

image = Image.open("hospitalwoman.jpg")
new_image4 = image.resize((150, 150))

st.sidebar.image([new_image3 ,new_image4])

st.sidebar.title("GRACE MEDICAL & DIAGNOSTICS")
st.sidebar.write("Located at Mab Global Estate, Gwarinpa.\nCALL/CHAT:08032092335. Email-Address: gracemedical@gmail.com")

st.sidebar.write("Welcome to GRACE MEDICAL AND DIAGNOSTICS, This is where your health is our utmost piority, you can use this app to communicate all your medical needs with us by filling the consultation form and you will get a prompt message from us as soon as you do so. All our medical practioners are on the stand to receive you and help you with utmost health service you need. WE CARE WHILE GOD CURES")

st.sidebar.write("# OUR SERVICES INCLUDES:")

st.sidebar.write("## DENTAL CLINIC")
st.sidebar.write("## FAMILY MEDICINE")
st.sidebar.write("## FERTILITY & GENETICS")
st.sidebar.write("## CHILD CLINIC")
st.sidebar.write("## GYNAECOLOGY")
st.sidebar.write("## MATERNITY")
st.sidebar.write("## SURGERY")

st.title("MEDICAL CONSULTATION FORM")

st.text_input("Prefix")

st.text_input("First Name")

st.text_input("Middle Name")

st.text_input("Last Name")

st.write("GENDER")
Male = st.checkbox("male")
Female = st.checkbox("female")
Others = st.checkbox("others")

st.text_input("AGE")

st.text_input("PHONE NUMBER")

st.write("## Have you seen a doctor for any of the following illness?")

st.write("High Blood Pressure")
yes = st.checkbox("YES")
no = st.checkbox("NO")

st.write("Heart Disease")
yes = st.checkbox("Yes")
no = st.checkbox("No")

st.selectbox("High Cholesterol", ["YES", "NO"])

st.selectbox("Diabetes", ["YES", "NO"])

st.selectbox("Bleeding disorder", ["YES", "NO"])

st.text_input("Others, Please Specify")

st.write("## Are You Allergic To Any Of This?(if any)")

Allergies = st.multiselect("Allergies: ",
                         ["Aspirin", "codeine", "sulfa drugs", "penicilin", "other antibiotics"])
 
st.text_input("State/Specify Reason For Consultation in Details")

st.selectbox("Have you ever undergone surgery?", ["Yes", "NO"])

image = Image.open("hospitalwoman.jpg")
new_image4 = image.resize((300, 300))

st.sidebar.image([new_image4])

st.sidebar.button("LEARN MORE ABOUT GRACE MEDICAL")

st.write("Upload Supporting Medical Reports(If Any)")

upload_file = st.file_uploader(label='Please upload your file', type=['.png', '.jpg', '.gif'])
        
d = st.date_input("Consultation Date(YYYY/MM/DD)")

t = st.time_input("Consultation Time(AM/PM)")

st.button("SEND")


