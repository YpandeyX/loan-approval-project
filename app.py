import streamlit as st
import pickle
import pandas as pd

try:
    model = pickle.load(open("loan_model.pkl", "rb"))
    st.success("Model Loaded Successfully")
except Exception as e:
    st.error(str(e))

st.title("Loan Approval Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

married = st.selectbox("Married", ["Yes", "No"])
married = 1 if married == "Yes" else 0

dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
dependents = {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents]

education = st.selectbox("Education", ["Graduate", "Not Graduate"])
education = 1 if education == "Graduate" else 0

self_employed = st.selectbox("Self Employed", ["Yes", "No"])
self_employed = 1 if self_employed == "Yes" else 0

applicant_income = st.number_input("Applicant Income", min_value=0)

coapplicant_income = st.number_input("Coapplicant Income", min_value=0)

loan_amount = st.number_input("Loan Amount", min_value=0)

loan_amount_term = st.selectbox(
    "Loan Amount Term (Months)",
    [12, 36, 60, 84, 120, 180, 240, 300, 360]
)

credit_history = st.selectbox("Credit History", ["Good", "Bad"])
credit_history = 1 if credit_history == "Good" else 0

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban", "Metro"]
)

property_area = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2,
    "Metro": 3
}[property_area]

if st.button("Predict"):
    data = pd.DataFrame([[gender, married, dependents, education,
                          self_employed, applicant_income,
                          coapplicant_income, loan_amount,
                          loan_amount_term, credit_history,
                          property_area]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")