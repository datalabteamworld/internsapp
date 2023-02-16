import streamlit as st
import pandas as pd

st.title("TAILOR'S AID")
st.header("welcome to Tailor's aid app")
st.write("this app helps you with measurement you need for cutting")

st.write("Lets get started")

name =st.text_input("Client's Name")

date =st.date_input("date of Measurement Taken")
types =st.selectbox("what are you designing for the client", ["Dress", "Blouse", "skirt"])
if types=="Dress":
    

    SH = st.number_input("shouldre in cm")
    L = st.number_input("length of dress")
    BR =st.number_input("bustround")
    UBR = st.number_input("uderbust round")
    HP = st.number_input("hip round")
    WR = st.number_input("waist round")
    HCR = st.number_input("halfcut round")
    SB = st.number_input("shoulder-bust")
    SUB =st.number_input("shoulder-underbust")
    SW = st.number_input("shoulder-waist")
    SHP = st.number_input("shoulder-hip")
    SK = st.number_input("shoulder-kneel")
    SL = st.number_input("sleeve length")
    SR = st.number_input("sleeve round")

    SH2 =SH/2
    BR2 =BR/4
    UBR2 =UBR/4
    HP2 =HP/4
    WR2 =WR/4
    SR2 =SR/2
    HCR2 =HCR/4

    list2 =[L,SH2,BR2,UBR2,HP2,WR2,SR2,SB,SW,SL,SK,SHP,SUB,HCR2]
    df2 = pd.DataFrame(list2, columns=["working measurement"], index=["L","SH2","BR2","UBR2","HP2","WR2","SR2","SB","SW","SL","SK","SHP","SUB","HCR2"])
    st.table(df2)


elif types=="skirt":
    L1 = st.number_input("length of skirt")
    HP = st.number_input("hip round")
    WR = st.number_input("waist round")
    HPL = st.number_input("hipline")
    
    HP1 =HP/4
    WR1 =WR/4
    
    list3 =[L1,WR1,HP1,HPL]
    df2 = pd.DataFrame(list3, columns=["working measurement"], index=["L1","WR1","HP1","HPL"])
    st.table(df3)

else:
   
    L3 = st.number_input("length of Blouse")
    SH = st.number_input("shouldre in cm")
    BR = st.number_input("Bustround")
    UBR = st.number_input("uderbust round")
    WR = st.number_input("waist round")
    HCR = st.number_input("halfcut round")
    SB = st.number_input("shoulder-bust")
    SUB = st.number_input("shoulder-underbust")
    SL = st.number_input("sleeve length")
    SR = st.number_input("sleeve round")
    SW = st.number_input("shoulder-waist")
    
    SH2 =SH/2
    BR2 =BR/4
    UBR2 =UBR/4
    WR2 =WR/4
    SR2 =SR/2
    
    

    list4 =[L3,SH2,BR2,UBR2,WR2,SR2,HCR,SB,SW,SL,]
    df4 = pd.DataFrame(list4, columns=["working measurement"], index=["L3","SH2","BR2","UBR2","WR2","SR2","HCR","SB","SW","SL",])
    st.table(df4)




