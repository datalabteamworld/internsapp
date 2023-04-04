from string import ascii_uppercase, digits
from random import choices


DAYS = [
    "Sunday",
    "Monday",
    "Teusday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]


LOCATION = [
    "Ikeja",
    "Akure",
    "Ikotun",
    "Osogbo",
    "Ilorin",
    "Ibadan",
    "Calabar",
    "Kano",
    "Zaria",
    "Abeokuta",
    "Warri",
    "Abuja",
]

DESTINATION = [
    "Ikeja",
    "Akure",
    "Ikotun",
    "Osogbo",
    "Ilorin",
    "Ibadan",
    "Calabar",
    "Kano",
    "Zaria",
    "Abeokuta",
    "Warri",
    "Abuja",
]


FLIGHT_CLASSES = ["First Class", "Business Class", "Economy Class"]


LOCAL_CSS = """
<style>div[data-testid="stExpander"] div[role="button"] p {
    font-size: 1.3rem;
}</style>
"""


def get_times():
    times = []

    for am in range(6, 13):
        times.append(f"{am} AM")

    for pm in range(1, 11):
        times.append(f"{pm} PM")
    return times

def generate_code():
    code = choices(ascii_uppercase + digits, k=6)
    
    return ''.join(code)