import pickle
import streamlit as st

# Load the pickled model and encoder
with open("my_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("my_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Define the inputs
country_options = ['N', 'Z ', 'Z', 'Ga', 'Ne', 'Ni', 'M', 'Ca', 'Nel', 'Ra', 'To', 'An', 'Rw', 'Mo']
gender_options = ['Male', 'Female']
age_options = ['36 - 40', '51-60', 'Above 60 years', '46 - 50', '41 - 45', '31 - 35', '26 - 30']
marital_options = ['Married', 'Single', 'Separated', 'Divorced']
prev_cred_options = ['No', 'Yes']

US_Duration = ['1 - 2', '3 - 4', 'Below 1 year', '5 and above']
Status = ['Lawful permanent resident', 'U.S. citizen', 'Nonimmigrant Visa Holder', 'Asylum or Refugee']
Education = ['College or University', 'High School', 'Middle School or Junior High School']
Children = [0, 2, 3, 1, 4, 5]
Bills = ['Yes', 'No']
Loan_Application = ['Yes', 'No']
Loan_Provider = ['Bank', 'Morgage Company', 'Credit unions ', 'Credit union', 'Microfinance institution', 'College ', 'Discover', 'Credit Union', 'Online lender', 'School']
Loan_Reason = ['Credit Cards', 'Home Mortgages', 'Just for testing the system ', 'Auto Loans', 'Credit card', 'Home mortgage', 'Auto loan', 'Student loans', 'Car loan', 'Personal loan']
Employment = ['Full-time', 'Part-time', 'Temporary or Contract Employee']
Salary = ['Income between $10,276 and $42,900', 'Income between $42,901 and $87,850', 'Income between $183,251 and $207,350', 'Income between $87,851 and $183,250', 'Income up to $10,275', '$10,276 - $42,900', '$42,901 - $87,850', '$183,251 - $207,350', '$87,851 - $183,250', '$87,851 -  $183,250']
Time_InUS = ['Below 1 year.', '1 - 2', '3 - 4', '5 and above', 'Below 1 year']
Credit = ['580-669', '670-739', '740-799', '300-579', "I didn't know", '800-850']
Loan_Amount = [3.00e+03, 5.00e+02, 1.00e+03, 2.50e+05, 2.00e+03, 4.00e+05, 1.00e+04, 1.00e+05,
 2.50e+03, 5.10e+03, 3.00e+05, 7.00e+02, 3.00e+04, 1.80e+04, 2.80e+05, 6.00e+02,
 1.50e+04, 1.20e+04, 2.00e+04, 1.82e+05, 1.20e+03, 4.00e+03, 1.70e+01, 2.50e+04,
 5.00e+03, 5.00e+04, 2.30e+05, 2.65e+05, 2.35e+04, 2.00e+05, 1.50e+03, 9.00e+03,
 2.05e+04]










# Define the app
def app():
    st.set_page_config(layout="wide")
    st.title("Loan Application Prediction")
    
    # Get user inputs
    country = st.selectbox("Country", options=country_options)
    gender = st.selectbox("Gender", options=gender_options)
    age = st.selectbox("Age", options=age_options)
    marital_status = st.selectbox("Marital Status", options=marital_options)
    prev_count_cred = st.selectbox("Previous Count of Credit", options=prev_cred_options)
    
    US_Duration_ = st.selectbox("US_Duration", options= US_Duration)
    Status_ = st.selectbox("Status", options=Status)
    Education_ = st.selectbox("Education", options=Education)
    Children_ = st.selectbox("Children", options=Children)
    Bills_ = st.selectbox("Bills", options=Bills)
    Loan_Application_ = st.selectbox("Loan_Application", options=Loan_Application)
    Loan_Provider_ = st.selectbox("Loan_Provider", options=Loan_Provider)
    Loan_Reason_ = st.selectbox("Loan_Reason", options=Loan_Reason)
    Employment_ = st.selectbox("Employment", options=Employment)
    Salary_ = st.selectbox("Salary", options=Salary)
    Time_InUS_ = st.selectbox("Time_InUS", options=Time_InUS)
    Credit_ = st.selectbox("Credit", options=Credit)
    Loan_Amount_ = st.selectbox("Loan_Amount", options=Loan_Amount)








    # Add submit button
    if st.button("Predict"):
        # Apply encoder
        encoded_inputs = encoder.transform([[country, gender, age, marital_status, prev_count_cred, US_Duration_, Status_, Education_, Children_, Bills_, Loan_Application_, Loan_Provider_, Loan_Reason_, Employment_, Salary_, Time_InUS_, Credit_, Loan_Amount_]])

        # Apply model
        prediction = model.predict(encoded_inputs)

        # Display the results
        if prediction == 1:
            st.markdown("### Result: Approved!")
        else:
            st.markdown("### Result: Denied.")

if __name__ == '__main__':
    app()
