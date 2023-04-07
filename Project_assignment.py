import streamlit as st
import calendar
from datetime import datetime

name = "";
layout = "centered"
st.title("Doctor Consultation Form")

years = [datetime.today().year, datetime.today().year+1, datetime.today().year+2]
months = list(calendar.month_name[1:])
day = list(calendar.day_name[1:])

with st.form("entry_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    col1.selectbox("Select Day:", day, key="day")
    col2.selectbox("Select Month:", months, key="month")
    col3.selectbox("Select Year:", years, key="year")

    "---"
    st.header("Patients Personal Information")
    colname, colsurname = st.columns(2)
    colname.text_input("First Name")
    colsurname.text_input("Last Name")

    "---"
    age = ["Age"]
    for x in age:
        st.number_input(f"{x}", min_value=0, format="%i", step=1, key=x)

    address = ["Address"]
    for x in address:
        st.text_input(f"{x}", placeholder="No 10, Egbeda, Lagos")


    illness = st.text_area("", placeholder="Give details of injury or illness...")




    firstaid = st.text_area("", placeholder="Details of any treatment or first-aid already administered")

    "---"

    submitted = st.form_submit_button("Save Data")

    if submitted:
        period = str(st.session_state["day"])+" "+str(st.session_state["month"])+" "+str(st.session_state["year"])
        name = {colname: st.session_state[colname]+" "+st.session_state[colsurname]}
        #age = {ages : st.session_state["Age"]}
        #address = {
#             address : st.session_state["Address"]



#                   }
#         st.write(f"Illness : {illness}")
#         st.write(f"First-Aid : {firstaid}")
#         st.success("Date Saved!")




