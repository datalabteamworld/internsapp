import streamlit as st
from PIL import Image
st.title('WAIST TO HIP RATIO CALCULATOR')
st.header('This application is used to calculate the Waist-to-Hip Ratio of a person')

img = Image.open('waist-hip-ratio.jpg')
st.image(img)

#brief introduction

st.subheader('Introduction')

st.markdown('''
The waist-to-hip ratio (WHR) calculation is one of the anthropometric measurements the doctor can take to check if excess weight is putting your health at risk. It determines how much fat is stored around your waist, hips, and buttocks.
As opposed to body mass index (BMI), which calculates the ratio of your weight to your height, WHR measures the ratio of your waist circumference to your hipcircumference.
This is vital because not all excess weight is the same when it comes to your health risks.

credit: https://www.healthline.com/health/waist-to-hip-ratio#advantages-of-whr

''')
#setting the input variables for the user

gender_selection = ['FEMALE', 'MALE']

gender = st.selectbox('Select your gender', options = gender_selection)
waist_circumference = st.number_input('Enter your waist circumference in inches: ')
hips_circumference = st.number_input('Enter your hips circumference in inches: ')

#definition of the WHR function:

def WHR(waist_circum, hips_circum):
    WHR = (waist_circum / hips_circum)
    WHR = '{:.2f}'.format(WHR)
    WHR = float(WHR)
    return WHR

#WHR = round((waist_circumference / hips_circumference),2)

if st.button('Calculate WHR'):
    WHR_val = WHR(waist_circumference, hips_circumference)
    if WHR_val > 0:
        if gender == 'FEMALE':
            if (WHR_val <= 0.80):
                st.success(f'Your waist-to-hip ratio is: {WHR_val}')
                st.write('\n You are at a low risk of heart disease and other conditions that are linked to being overweight')
                st.subheader('\n Recommendations!')
                st.write('\n1. Maintain a health lifestyle of a balanced diet and exercise 3 days/week.')
                st.write('\n2. Consume not less than 3 litres of water intake per day.')
                st.write('\n3. Avoid late night meals.')
            elif (WHR_val >=0.81 and WHR_val <=0.85):
                st.success(f'Your waist-to-hip ratio is: {WHR_val}')
                st.write('\n You are at a moderate risk of heart disease and other conditions that are linked to being overweight')
                st.subheader('\n Recommendations!')
                st.write('\n1. Adjust your diet to contain more vegetables, fibre and cook with trans-fat oils.')
                st.write('\n2. Exercise more, ones that engage your mid-section, 10 - 15 minutes cardio/day and squats for regions below the torso.')
                st.write('\n3. Avoid late night meals.')
                st.write('\n4. Cut down on alcohol.')
                st.write('\n5. Drink at least 4 litres of water per day. Water can be cold, well above room temperature but not iced.')
                st.write('\n6. See you doctor to discuss your findings and get further recommendations.')
              
            elif (WHR_val >= 0.86):
                st.success(f'Your waist-to-hip ratio is: {WHR_val}')
                st.write('\n You are at a high risk of heart disease and other conditions that are linked to being overweight')
                st.subheader('\n Recommendations!')
                st.write('\n1. Please see your doctor or dietician to discuss your findings.')
                st.write('\n2. Exercise at least, 4 days a week - from cardio to core/mid-section and lower body exercises.')
                st.write('\n3. Adjust diet to contain more vegetables, fibre, and plant or fish protein. Adjust cooking method also.')
                st.write('\n4. Portion control is important.')
                st.write('\n5. Avoid alcohol and cigarettes or any other substitute.')
                st.write('\n6. Drink at least, 4 litres of water in a day. Water can be cold, i.e well above room temperature, but not iced.')
                st.write('\n7. Avoid late night meals completely.')

        if gender == 'MALE':
            if (WHR_val <= 0.95):
                st.success(f'Your waist-to-hip ratio is: {WHR_val}')
                st.write('''\n You are at a low risk of heart disease and other conditions that are linked to being overweight''')
                st.subheader('\n Recommendations!')
                st.write('\n- Maintain a health lifestyle of a balanced diet and 3 days/week exercise.') 
                st.write('\n- Increase water intake to not less than 3 litres per day.')
                st.write('\n- Avoid late night meals.')
    
            elif (WHR_val >=0.96 and WHR_val <=0.99):
                st.success(f'Your waist-to-hip ratio is: {WHR_val}')
                st.write('''\n You are at a moderate risk of heart disease and other conditions that are linked to being overweight.''')
                st.subheader('\n Recommendations!')
                st.write('\n- Adjust your diet to contain more vegetables, fibre and cook with trans-fat oils.')
                st.write('''\n- Do more exercises that engage your mid-section, 10 - 15 minutes cardio per day and squats for regions below the torso.''')
                st.write('\n- Avoid late night meals.')
                st.write('\n- Cut down on alcohol.')
                st.write('''\n- Drink at least 4 litres of water per day. Water can be cold, well above room temperature but not iced.''')
                st.write('\n6. See you doctor to discuss your findings and get further recommendations.')
            elif (WHR_val >= 1.00):
                st.success(f'Your waist-to-hip ratio is: {WHR_val}')
                st.write('\n You are at a high risk of heart disease and other conditions that are linked to being overweight')
                st.subheader('\n Recommendations!')
                st.write('\n- Please see your doctor or dietician to discuss your findings.')
                st.write('\n- Exercise at least, 4 days a week - from cardio to core/mid-section and lower body exercises.')
                st.write('\n- Adjust diet to contain more vegetables, fibre, and plant or fish protein. Adjust cooking method also.')
                st.write('\n- Portion control is important.')
                st.write('\n- Avoid alcohol and cigarettes or any other substitute.')
                st.write('\n- Drink at least, 4 litres of water in a day. Water can be cold, i.e well above room temperature, but not iced.')
    
    else:
        st.error('ERROR!!! Please check the value of waist and hip circumference.')
        
st.text('''

''')

st.caption('''**More About How WHR Relates to your Well Being**''')
st.caption('''According to a 2021 article by healthline, a 2021 study showed that people who carry more of their weight around their midsection (an apple-shaped body) may be at a higher risk of heart disease, type 2 diabetes, and premature death than people who carry more of their weight in their hips and thighs (a pear-shaped body). Even if your BMI is within a moderate range, your risk of disease may be increased.''')

st.caption('''According to the World Health Organization (WHO), a moderate WHR is:

>0.9 or less in men

>0.85 or less for women
In both men and women, a WHR of 1.0 or higher increases the risk of heart disease and other conditions that are linked to having overweight
Some advantages of WHR is that is easy, inexpensive and an accurate way to see the proportion of your body fat. It can also help predict your risk of heart disease and diabetes.
Research from the American Diabetes Association suggested that WHR is even more accurate than BMI for predicting the risks of cardiovascular disease and premature death.

Some disadvantages include:

It’s easy to make mistakes while checking WHR, because you need to take two separate measurements. And, it can be hard to get an accurate measurement of your hips.

WHR can also be harder to interpret than waist circumference — another measurement of abdominal obesity. You might have a high WHR because you carry more weight in your abdomen. Or, you might simply have extra muscle around your hips from working out.

Certain people won’t be able to get an accurate measure using WHR, including people who are shorter than 5 feet tall and people who have a BMI of 35 or higher. WHR is also not recommended for use in children.
''')
            
st.caption('''In summary:''')
st.caption('''
Waist-to-hip-ratio is a quick and easy way to check how much weight you carry around your middle. It’s just one of several measures — along with BMI — that your doctor can use to evaluate your weight and health.

Use it as a guide to talk with your doctor about managing your weight and disease risk factors

source: https://www.healthline.com/health/waist-to-hip-ratio#advantages-of-whr
''')
