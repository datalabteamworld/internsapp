import streamlit as st
from PIL import Image

img = Image.open('new.jfif')
st.image(img)

st.title("KOREAN SERIES RATING")

st.selectbox("What is your gender", ["Male", "Female"])
st.selectbox("What is your favourite korean movie", ["None", "Squid Game", "Extraordinary Attorney Woo", "Vincenzo", "Alchemy of Souls", "Lawless Lawyer", " Under the Queen's Umbrella", "Business Proposal" "Boys Over Flowers"])

st.text_input('If your favourite movie isnt above, kindly input it below.')

st.slider("Rate your favourite movie",0,10)
st.text_input('Kindly recommend a movie/series for other kdrama lovers')

st.button('SUBMIT')

st.text('THANK YOU FOR YOUR FEEDBACK')