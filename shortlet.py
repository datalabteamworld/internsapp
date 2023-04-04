#Importing required libraries
import streamlit as st

#Adding title and header to app
st.title("A.T Short Let Apartment App")

st.header("Welcome to A.T Short Let Serviced Apartment")

#Creating a subheader to sidebar
st.subheader("Home away from Home")

#Adding image to the app
from PIL import Image

image1 = Image.open("shtlet4.jpg")

st.image(image1)

#Creating mission statement under each image
st.write("Identifying the need for a comfortable and private home away from home birth the inovation of AT Short Let Serviced Apartment to fulfil the need of a comfy, private place.")

image2 = Image.open("shtlet3.jpg")

st.image(image2)
         
st.write(" The accommodations are available in a variety of layouts, styles and sizes, at attractive prices, offering the perfect solution for those in need of temporary housing.")

image3 = Image.open("shtlet1.jpg")

st.image(image3)

st.write("Through our stylish offer, our passion, and our focus on quick and straightforward living solutions, we bring fun and enjoyment to the lives of our clients and employees.")

#Creating sidebar content to gather data for booking         
st.sidebar.subheader("Make your Booking here")

#Adding a text input widget
FirstName = st.sidebar.text_input("First name")
LastName = st.sidebar.text_input("Last name")
ContactNumber = st.sidebar.text_input("Contact number")
Email = st.sidebar.text_input("Email")

#Adding date input widget
x = st.sidebar.date_input("Arrival date")
y = st.sidebar.date_input("Departure date")
z = (y-x)

#Adding number input widget
st.sidebar.number_input("Adult", step = 1)
st.sidebar.number_input("Children", step = 1)
st.sidebar.number_input("Infant", step = 1)
    

st.sidebar.write(f"You are booking for {z} days")

st.sidebar.write("Select your Apartment")

#Adding columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.sidebar.button("Basic"):
         st.sidebar.selectbox("Basic",["Basic Studio Apartment","Luxury Studio Apartment"])
        
with col2:
    if st.sidebar.button("1 Bedroom"):
        st.sidebar.selectbox("1 Bedroom",["1 Bedroom Standard Apartment", "Luxury 1 Bedroom Apartment"])
                             
with col3:
    if st.sidebar.button("2 Bedroom"):
        st.sidebar.selectbox("2 Bedroom"["2 Bedroom Standard Apartment","Luxury 2 Bedroom Apartment"])
        
with col4:
    if st.sidebar.button("3 Bedroom"):
        st.sidebar.selectbox("3 Bedroom"["3 Bedroom Standard Apartment","Luxury 3 Bedroom Apartment"])

st.sidebar.text_input("Special Requirement")
                      
if st.sidebar.button("Book"):
    st.sidebar.write("Continue to Payment")
    
else:
    st.sidebar.button("Book on Hold")

PaymentMethod = st.sidebar.selectbox("PaymentMethod", ["Card", "Paypal", "Bank transfer(automatic)"])

col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("Card"):
        st.radio("Card",["Visa", "Verve", "Mastercard"])

with col2:
    if st.button("Paypal"):
        st.text_input("Paypal email")
                                            
if st.sidebar.button("Pay"):
    st.sidebar.success(f"You have successfully booked for {z} days")
    