import streamlit as st

from PIL import Image

img = Image.open("Abuja logo.jpg")
st.sidebar.image(img, width = 350)



st.header("WELCOME TO UNIVERSITY OF ABUJA ADMISSION PORTAL")

st.title("Please kindly fill the below information for your admission status")
          

    
    


Candidate_name = st.text_input("Name")
Jamb_scores = st.number_input("Jamb score", step = 1)
Waec_result = st.selectbox("Do yo have WAEC result?", ["Yes", "No"])



        

 
    
if st.button("Check admission status"):
   


    if Jamb_scores > 250 and Waec_result == Yes:
        st.write(f'Congratulations.\n You have been offered admission')
    elif Jamb_scores > 250 and Waec_result == No:
        st.write(f'Congratulations.\n You have been offered admission')
    elif Jamb_scores != 250 and Waec_result == Yes:
        st.write(f'Wait for the next admission list')
    elif Jamb_scores != 250 and Waec_result == No:
        st.write(f'Not qualified to be admitted')
   
    else:
        st.write(f'Not qualified to be admitted')
        
     

            
              
            


   





 

            

            
           
             
             

                          
             


