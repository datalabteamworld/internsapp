import streamlit as st
from PIL import Image
#img = Image.open("streamlit.png")

st.title("Welcome to Ibot Tax calculator  App")
st.image("tax1.PNG.png", width = 250)


st.header('Tax calulator applicable in Scotland')
st.subheader('This tax calculator is based on the current tax 2023 tax law applicable in scotland')

while True:
    try:

        income = (st.number_input("Please enter your gross income in Pounds: "))
    except ValueError:
        st.error("Sorry, We didn't understand that please enter gross income as a number")

        continue
    else:
        break
if income <= 12570:
    tax = 0

elif income <= 14732:
    tax = (income - 12570) * 0.19

elif income <= 27850:
    tax = (income - 14732) * 0.20 + 410.78

elif income <= 58942: 
    tax = (income - 27850) * 0.21 + (2623.60 + 410.78)

elif income <= 208942: 
    tax = (income - 58942) * 0.41 + (6529.32 + 2623.60 + 410.78)

else:
    tax = (income - 208942) * 0.46 + (61500 + 6529.32 + 2623.60 + 410.78)


net_income = income - tax    

monthly_take_home = round(net_income/12,2)

if tax == 0:
    monthly_tax = 0
else:
    monthly_tax = tax/12
        
if(st.button("Calculate tax for the year")):
    st.text("Your tax for the year is {}.".format(tax))
    st.success("calculation succesful🔥🔥🔥🔥🔥")
    
st.sidebar.write("You can contact the below email for any further clarification") 
st.sidebar.write("Datalabs@info.com")

st.sidebar.write("Please note that there could be other statutory deductions like NI, Pension etc... that could further affect your take home")


st.sidebar.write("Do watch out for our next version coming soon with other fantastic functions below:")   

st.sidebar.write("NI calculation, Track future expenses, Plan savings & Forcast future spendings")


if(st.button("Calculate net income for the year")):
    st.text("Your net income for the year is {}.".format(net_income))
    st.success("Calculation succesful🔥🔥🔥🔥🔥")
          
if(st.button("Calculate your monthly take home")):
    st.text("Your monthly take home is {}.".format(monthly_take_home))
    st.success("Calculation succesful🔥🔥🔥🔥🔥🔥")
    
if(st.button("calculate your monthly tax")):
    st.text("Your monthly tax is {}.".format(monthly_tax))
    st.success("Calculation succesful🔥🔥🔥🔥🔥🔥")
    

st.text("kindly rate you experience from 1 - 10 (1 being lowest and 10 heighest)")   
st.select_slider('Slide me', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
st.text_input('We want to hear from you please give feedback')
st.warning('To willfully fail to pay taxes is a federal offense under the Internal Revenue Service (IRS) tax code')
                 