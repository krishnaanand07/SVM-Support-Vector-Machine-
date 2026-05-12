import streamlit as st
import pickle
import numpy as np

# Load model
data = pickle.load(open("svm_model.pkl", "rb"))

model = data["model"]

st.title("Customer Churn Prediction")

st.write("Enter Customer Details")

# Inputs
age = st.number_input("Age")

gender = st.selectbox("Gender", ["Male", "Female"])

region = st.selectbox(
    "Region",
    ["North", "South", "East", "West"]
)

monthly_income = st.number_input("Monthly Income")

subscription_length = st.number_input("Subscription Length")

monthly_bill = st.number_input("Monthly Bill")

support_tickets = st.number_input("Support Tickets")

internet_usage = st.number_input("Internet Usage GB")

contract_type = st.selectbox(
    "Contract Type",
    ["Monthly", "Yearly"]
)

payment_method = st.selectbox(
    "Payment Method",
    ["Credit Card", "Debit Card", "UPI", "Cash"]
)

multiple_services = st.selectbox(
    "Has Multiple Services",
    ["Yes", "No"]
)

last_login = st.number_input("Last Login Days Ago")

satisfaction_score = st.number_input("Satisfaction Score")

# Encoding manually
gender = 1 if gender == "Male" else 0

region_map = {
    "North": 0,
    "South": 1,
    "East": 2,
    "West": 3
}

region = region_map[region]

contract_type = 1 if contract_type == "Yearly" else 0

payment_map = {
    "Credit Card": 0,
    "Debit Card": 1,
    "UPI": 2,
    "Cash": 3
}

payment_method = payment_map[payment_method]

multiple_services = 1 if multiple_services == "Yes" else 0

# Predict
if st.button("Predict"):

    input_data = np.array([[
        age,
        gender,
        region,
        monthly_income,
        subscription_length,
        monthly_bill,
        support_tickets,
        internet_usage,
        contract_type,
        payment_method,
        multiple_services,
        last_login,
        satisfaction_score
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Not Churn")