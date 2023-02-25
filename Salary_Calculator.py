import streamlit as st
st.title("Salary Calculation App")

st.text(" ")
st.text(" ")

Minwage = st.sidebar.number_input("What is your country's minimum wage", step = 1)
YearsofExp = st.sidebar.number_input("How many years of work experience do you have", step = 1)
Skillprof = st.sidebar.radio("What is your skill proficiency level", [0,1,2,3,4,5])

col1, col2 = st.columns(2, gap="large")

with col1:

    st.selectbox("Course of study", ["Accounting", "Banking and Finance", "Business Administration", "Communications", "Computer Science", "Economics", "Law", "Medicine", "Political Science", "Zoology"])

    st.selectbox("Preferred Industry", ["Aviation", "Agriculture", "Arts", "Banking", "Consultancy", "Education", "E-commerce", "Energy", "Entertainment", "Fashion", "Computer Science", "Health", "Hospitality and Tourism", "Information", "Law", "Manufacturing", "NGO", "Public Sector", "Startup", "Telecommunications"])

    st.selectbox("Area of Interest", ["Adminitration", "Accounting", "Customer Service", "Relationship Management", "Human Resources", "Legal", "Operations", "Marketing/Sales", "Product", "Software Development", "Supply Chain", "Startup", "UI/UX Designer"])

    st.selectbox("Major Skill/Software", ["Business Analysis", "Business Development", "Communication", "CRM/Saleforce", "Data Analysis", "Data science", "Digital Marketing", "G-suite", "Economics", "Law", "Microsoft Office", "Writing", "Web Development" "Project Management", "Social Media Management", "Graphic Design"])

with col2:
    
    st.radio("What is your age range", ["18-25", "26-35", "36-45", "46-65"])

    st.radio("Identification Type", ["National Identity Card", "International Passport", "Driver's Licence", "Worker's/Resident Permit", "Voter's Card"])

    st.number_input("Please enter your ID Number", step = 1)

st.text(" ")
st.text(" ")
st.text(" ")
    
st.checkbox("Would you like us to match you with an employer?")

st.write('PLEASE NOTE:')

st.write('For Years of Experience < 7,')
st.write('Sal = Minwage * YearsofExp * Skillprof')

st.write('For Years of Experience > 7 <= 15,')
st.write('Sal = (Minwage*1.5) * YearsofExp * Skillprof')

st.write('For Years of Experience > 15,')
st.write('Sal = (Minwage*2) * YearsofExp * Skillprof')


if st.button("Calculate Salary"):
    Sal = Minwage*YearsofExp*Skillprof
   
    st.write(f'Your Salary Expectation is  {Sal}. \n We will verify your information and send you an approval or unverified email within 5 to 10 working days. \n If the information provided is correct, your verification certificate will be uploaded on the National Job Board. \n All the best!')
            
             