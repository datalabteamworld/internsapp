import streamlit as st
import time

# Application that books flights for employees and gives a discount

#Calculate discounted flight fee
def Flight_fee (actual_price,discount):
    discount = actual_price * (discount/100)
    final_price = actual_price - discount
    return final_price


st.image("https://leadership.ng/wp-content/uploads/2022/08/Air-travel-flight.jpg")
st.title ("Employee Flight Booking")
st.header ("Employees get a 20% discount when using this app to book their flights")

# employee details
col1, col2 = st.columns(2)
with col1:
    employee_name = st.text_input("Enter Name:")
with col2:
    employee_email = st.text_input("Enter Email:")
col1, col2 = st.columns(2)
with col1:
    employee_contact_number = st.text_input("Enter Contact Number:")
with col2:
    employee_department = st.selectbox("Select Department", ["Pick Department", "Engineering", "Accounting", "Security", "Programming", "Human Resources"])
employee_passport_upload = st.file_uploader("Please upload a valid Passport data page:")

#flight booking
flight_type = st.radio("Which flight do you which to book:", (" ","Local","International"))

if flight_type == "International":
    st.warning("Sorry there are currently no International flights availabe")
    
elif flight_type == "Local":  
    col1, col2, col3 = st.columns(3)
    with col1:
        Date = st.date_input("Select intended Departure date")
    with col2:
        Departure = st.selectbox("Your Departure Location", ["Select Departure", "Abuja", "Asaba", "Benin", "Calabar", "Enugu", "Jigawa", "Kaduna", "Lagos", "Warri"])
    with col3:
        Destination = st.selectbox("Your Destination", ["Select Destination", "Abuja", "Asaba", "Benin", "Calabar", "Enugu", "Jigawa", "Kaduna", "Lagos", "Warri"])
    
    if Departure == "Select Departure":
        st.warning("Please select a valid Departure point")
        
    elif Destination == "Select Destination":
        st.warning("Please select a valid Destination point")
        
    else:
        st.success("Your Departure point and Destination has been selected, here are available flights")
    
        Airlines = st.selectbox("Available Airlines", ["Select Airline", "Airpeace", "Arik", "Aero"])
        if Airlines == "Select Airline":
            st.warning("Please select a valid Airline")
        elif Airlines == "Airpeace":        
            flight_type1 = st.radio("Which flight do you want to book", ("Standard Class", "First Class", "Executive Class", "Presidential Class"))
            if flight_type1 == "Standard Class":
                price = 65000
                st.success("Standard Class Selected")
                st.write("Price:", price)
                
            elif flight_type1 == "First Class":
                price = 165000
                st.success("First Class Selected")
                st.write("Price:", price)
            elif flight_type1 == "Executive Class":
                price = 290000
                st.success("Executive Class Selected")
                st.write("Price:", price)
            elif flight_type1 == "Presidential Class":
                price = 380000
                st.success("Presidential Class Selected")  
                st.write("Price:", price)
                
            button = st.button("Book Flight ")
            if button:
                with st.spinner("Booking Flight..."):
                    time.sleep(2)
                st.success("Your flight has been booked succesfully, payment is due within 2 hours of booking.")
                discounted_price = Flight_fee(price,20)
                st.write(employee_name, "Your discounted price is", discounted_price, "flight schedule and details on how to make payemnt has been forwarded to", employee_email)
                
        elif Airlines == "Arik":  
            flight_type2 = st.radio("Which flight do you want to book", ("Standard Class", "First Class", "Executive Class", "Presidential Class"))
            if flight_type2 == "Standard Class":
                price = 70000
                st.success("Standard Class Selected")
                st.write("Price:", price)
                
            elif flight_type2 == "First Class":
                price = 180000
                st.success("First Class Selected")
                st.write("Price:", price)
            elif flight_type2 == "Executive Class":
                price = 300000
                st.success("Executive Class Selected")
                st.write("Price:", price)
            elif flight_type2 == "Presidential Class":
                price = 400000
                st.success("Presidential Class Selected")  
                st.write("Price:", price)
                
            button = st.button("Book Flight ")
            if button:
                with st.spinner("Booking Flight..."):
                    time.sleep(2)
                st.success("Your flight has been booked succesfully, payment is due within 2 hours of booking.")
                discounted_price = Flight_fee(price,20)
                st.write(employee_name, "Your discounted price is", discounted_price, "flight schedule and details on how to make payement has been forwarded to", employee_email)
        elif Airlines == "Aero":   
            flight_type3 = st.radio("Which flight do you want to book", ("Standard Class", "First Class", "Executive Class", "Presidential Class"))
            if flight_type3 == "Standard Class":
                price = 60000
                st.success("Standard Class Selected")
                st.write("Price:", price)
                
            elif flight_type3 == "First Class":
                price = 150000
                st.success("First Class Selected")
                st.write("Price:", price)
            elif flight_type3 == "Executive Class":
                price = 270000
                st.success("Executive Class Selected")
                st.write("Price:", price)
            elif flight_type3 == "Presidential Class":
                price = 370000
                st.success("Presidential Class Selected")  
                st.write("Price:", price)
                
            button = st.button("Book Flight ")
            if button:
                with st.spinner("Booking Flight..."):
                    time.sleep(2)
                st.success("Your flight has been booked succesfully, payment is due within 2 hours of booking.")
                discounted_price = Flight_fee(price,20)
                st.write(employee_name, "Your discounted price is", discounted_price, "flight schedule and details on how to make payemnt has been forwarded to", employee_email)
                

