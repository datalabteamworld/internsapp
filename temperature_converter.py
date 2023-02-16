import streamlit as st

st.title('Temperature Converter')

option = st.radio('What type of conversion', ('Fahrenheit to Celcius', 'Celcius to Fahrenheit'))

temp = st.number_input('Enter Temperature')

def calc_temp(temp):
    
    if option == 'Fahrenheit to Celcius':
        ans = round((temp - 32)/1.8, 2)
        st.write(f'Your temperature is {ans} Celcius')
    elif option == 'Celcius to Fahrenheit':
        ans = round(1.8*temp + 32, 2)
        st.write(f'Your temperature is {ans} Fahrenheit')
    else:
        st.write(f'Invalid temperature or option')
        
def app():
    calc_temp(temp)
    
if __name__=='__main__':
    app()