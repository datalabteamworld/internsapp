import streamlit as st
from PIL import Image

img = Image.open('bank image.jpg')
st.sidebar.image(img)

img = Image.open('debit card images.jpg')
st.sidebar.image(img)

img = Image.open('./banklogo.jpg')
st.image(img,width=100)
        
st.header("WELCOME TO P&G BANK'S COMPLAINT RESOLUTION PORTAL")

st.write("Kindly fill out the form below to enable us treat your complaint promptly")
    
Name = st.text_input("Name ")

Phone_Number = st.text_input("Phone Number ")

Account_Number = st.text_input("Account Number ")

Complaint_Type = st.selectbox("Complaint Type",["Failed Transfers", "Failed ATM/POS Debits", "Poor Customer Experience"])

if Complaint_Type == "Failed Transfers":

    Beneficiary_Account_Number = st.text_input("Beneficiary Account Number ")
    
    Beneficiary_Bank = st.text_input("Beneficiary Bank ")
    
    Amount = st.text_input("Amount ")
    
    Transaction_Date = st.date_input("Transaction Date")
    
    if st.button("Submit"):
    
        st.write(f"Your Complaint is received, feedback will be provided in 24 working hours. Thank you.")
    
elif Complaint_Type == "Failed ATM/POS Debits":
    
    Debited_Amount = st.text_input("Debited Amount ")
    
    Masked_Card_Pan = st.text_input("Card Pan ")
    
    Date_of_Transaction = st.date_input("Date of Transaction")
    
    if st.button("Proceed"):
    
        st.write(f"Your Complaint is received, feedback will be provided within 3 business days. Thank you.")
    
else :
    Tpye_Your_Complaint = st.text_input("Type Your Complaint ")
    
    st.button("Feedback")
    
    st.write(f"We apologize for the not so pleasant experience you have had, be rest assusred that prompt action will be taken. Thank you for your honest feedback.")
    