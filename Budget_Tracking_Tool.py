import streamlit as st
import pandas as pd

def write_to_csv(date, category, expense):
    # write data to csv file
    with open('budget.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([date, category, expense])

def read_from_csv():
    # read data from csv file
    df = pd.read_csv('budget.csv', names=['date', 'category', 'expense'])
    return df

def main():
    st.set_page_config(page_title='Budget Tracker', page_icon=':money_with_wings:')

    # create sidebar
    st.sidebar.title('Budget Tracker')
    page = st.sidebar.selectbox('Select a page', ['Home', 'View Expenses'])

    # create main content
    if page == 'Home':
        st.header('Enter Expense')
        with st.form(key='my_form'):
            col1, col2, col3 = st.columns(3)
            with col1:
                category = st.text_input('Category')
            with col2:
                expense = st.number_input('Expense', value=0.0, step=0.01)
            with col3:
                date = st.date_input('Date')
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            write_to_csv(date, category, expense)
            st.success('Expense added successfully!')

    elif page == 'View Expenses':
        st.header('View Expenses')
        df = read_from_csv()
        st.dataframe(df)

if __name__ == '__main__':
    main()
