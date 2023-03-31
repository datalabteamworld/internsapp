import streamlit as st
import datetime 
from PIL import Image

image = Image.open('Bednbreakfast.jpg')
                                   
st.sidebar.image(image, width= 300)

st.sidebar.radio('Signup', ('as Guest', 'as Host'))
          
                                     
st.title(':green[Bed & Breakfast] :orange[NG]')
st.markdown("**Apartment Booking Application**")                         

st.selectbox("Category", ("Studio", "Apartment", "Party House"))

st.selectbox("Choose location", ('Abuja', 'Akwaibom', 'Delta', 'Edo', 'Crossriver', 'Lagos'))  

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.selectbox("No. of bedroom", (1,2,3,4,5,6))

col2.selectbox("Type", ('Furnished', 'Shared', 'Serviced'))

col3.date_input("Check-in date", datetime.date(2023, 2, 14))
   
col4.date_input("Check-out date", datetime.date(2023, 2, 14))
    
col5.time_input('Check-in time', datetime.time(1, 0))
    
col6.time_input('Check-out time', datetime.time(12, 0))  

Num_of_nights = st.number_input('Number of nights', step = 1)

rate = st.number_input('Nightly rate _(10% inclusive)_', step = 1000)
Total_amount = Num_of_nights * rate
commission = (Total_amount*(10 / 100))


if st.button("Total amount"):
    Result = commission + Total_amount
    st.write(f'{Result}')
    
  
with st.form("my_form"):
    emailaddress = st.text_input('Email address')
    password = st.text_input('Phone no.')
    st.form_submit_button('Complete booking')     

    
    
    
    
