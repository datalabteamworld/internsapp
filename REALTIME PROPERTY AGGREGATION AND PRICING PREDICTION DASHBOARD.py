import streamlit as st
import datetime
from PIL import Image

img = Image.open("mansionseaside.jpg")
st.image(img, width=500)
st.title('PROPERTIES BEST PRICING DEAL')
st.subheader("With our property dashboard, we promise best and agreegated pricing ever")
interest= st.selectbox("Please select your desired property type:", ['rent', 'buy','lease'])
#if interest=="rent":
#    interest=st.text('select apartment type')
#if interest=='buy':
#    interest=st.text('select property type')
#elif interest=='lease':
#    interest=st.text('select property type')

interest2= st.selectbox("indicate property types:", ['Mansionnaite', 'duplex','land' ,'bungalow'])
#if interest2=="Mansionnaite":
#        interest2=st.text('see available mansions')

#elif interest2=="duplex":
#        interest2=st.text('see available duplexes')
        
#elif interest2== "land":
#       interest2=st.text('see available land')
        
#elif interest2=="bungalow":
#        interest2=st.text('see available bungalow') 
        
Location= st.selectbox("indicate property location:", ['England', 'whales', 'Scotland' ,'Ireland'])
#if Location=="England":
#        Location=st.text('see available properties')

#elif Location=="whales":
#        Location=st.text('see available properties')
        
#elif Location== "Scotland":
#       Location=st.text('see available properties')
        
#elif Location=="Ireland":
#        Location=st.text('see available properties') 
        
        
image = Image.open('seaside.jpg')
st.image(image, caption='front sea views')
image = Image.open('mansionseaside.jpg')
st.image(image, caption='front elevation')
image = Image.open('countryside.jpg')
st.image(image, caption='garden view')
image = Image.open('castle.jpg')
st.image(image, caption='castlerock')


#viewing_date = st.date_input("Please select viewing date", min_value=datetime.date(1921, 1, 1),
# max_value=datetime.date(2030, 12, 31))
 

Priceaggregatebydate = st.date_input(
     "Please confirm the time stamp you want your agreegated property prices",
     datetime.date(2019, 7, 6))
st.write('Based on your property preferences for this time:', Priceaggregatebydate)

st.text("We will redirect to your customized dashboard where you will see realtime pricing for your choosing property preferences")