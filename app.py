import streamlit as st
from email_validator import validate_email
from utils import (
    DAYS,
    DESTINATION,
    FLIGHT_CLASSES,
    LOCAL_CSS,
    LOCATION,
    get_times,
    generate_code,
)

st.set_page_config(page_title="Flight Booking App", page_icon=":plane")


def clear_input():
    st.session_state["location"] = "Select"
    st.session_state["destination"] = "Select"
    st.session_state["flight_class"] = "Select"
    st.session_state["seats"] = 1
    st.session_state["day"] = "Select"
    st.session_state["time"] = "Select"
    st.session_state["name"] = ""
    st.session_state["card_number"] = ""
    st.session_state["phone_number"] = ""
    st.session_state["email"] = ""


LOCATION.sort()
DESTINATION.sort()

st.markdown(LOCAL_CSS, unsafe_allow_html=True)


st.sidebar.title("About the App")
st.sidebar.write("A web app that help users to book flight easily and efficiently.")


# start the user interface
st.title("Flight Booking App")

if "form_expanded" not in st.session_state:
    st.session_state.form_expanded = False

with st.expander("Booking details", True):
    # with st.form("flight_form"):
    fcol1, fcol2 = st.columns(2)

    with fcol1:
        location = st.selectbox(
            "Pick your location", key="location", options=["Select"] + LOCATION
        )
        destination = st.selectbox(
            "Pick your destination", key="destination", options=["Select"] + DESTINATION
        )

        flight_class = st.selectbox(
            "Pick your preferred flight class",
            key="flight_class",
            options=["Select"] + FLIGHT_CLASSES,
        )

    with fcol2:

        seats = st.number_input(
            "Enter the number of seats", step=1, min_value=1, key="seats"
        )
        day = st.selectbox("Pick day of flight", options=["Select"] + DAYS, key="day")
        time = st.selectbox(
            "Pick time of flight", options=["Select"] + get_times(), key="time"
        )

    if st.button("Next"):
        # st.write("form submitted")
        if location == "Select":
            st.error("Please select where you are taking the flight from")
            st.stop()

        if destination == "Select":
            st.error("Please select your destination")
            st.stop()

        if location == destination:
            st.error("Location cannot be the same as destination")
            st.stop()

        if flight_class == "Select":
            st.error("Please select your preferred flight class")
            st.stop()

        if day == "Select":
            st.error("Please select day of flight")
            st.stop()
        if time == "Select":
            st.error("Please select time of flight")
            st.stop()

        st.session_state.form_expanded = True


with st.expander("Profile Details", st.session_state.form_expanded):

    pcol1, pcol2 = st.columns(2)

    with pcol1:
        name = st.text_input("Enter your name", key="name").strip()
        card_number = st.text_input(
            "Enter your ID card number", key="card_number"
        ).strip()

    with pcol2:
        phone_number = st.text_input(
            "Enter your mobile number", key="phone_number"
        ).strip()
        email = st.text_input("Enter your email address", key="email").strip()

    if st.button("Book Flight"):
        if not name:
            st.error("Name is required")
            st.stop()

        if not phone_number:
            st.error("Mobile number is required")
            st.stop()

        if not phone_number.isnumeric() or len(phone_number) != 11:
            st.error("Phone number is invalid")
            st.stop()

        if not card_number:
            st.error("ID card number is required")
            st.stop()

        if not email:
            st.error("Email is required")
            st.stop()

        try:
            email = validate_email(email)
        except Exception as error:
            print(error)
            st.error("Please enter a valid email address")
            st.stop()

        st.success(
            f"Your flight has been successfully booked. Your booking code is: {generate_code()}"
        )
        st.info("Note: all flights missed will have to be rescheduled.")

st.button("Clear data", on_click=clear_input)
