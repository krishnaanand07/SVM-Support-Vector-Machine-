import streamlit as st
import pickle
import numpy as np

# Load model
data = pickle.load(open("svm_model.pkl", "rb"))

model = data["model"]

# Title
st.title("Customer Churn Prediction using SVM")

st.write("Enter customer details below")

# Input fields
age = st.number_input("Age", min_value=1)

monthly_income = st.number_input("Monthly Income", min_value=0.0)

subscription_length = st.number_input(
    "Subscription Length Months",
    min_value=0
)

monthly_bill = st.number_input("Monthly Bill", min_value=0.0)

support_tickets = st.number_input("Support Tickets", min_value=0)

internet_usage = st.number_input(
    "Internet Usage GB",
    min_value=0.0
)

last_login = st.number_input(
    "Last Login Days Ago",
    min_value=0
)

satisfaction_score = st.number_input(
    "Satisfaction Score",
    min_value=0.0
)

# Predict button
if st.button("Predict"):

    input_data = np.array([[
        age,
        monthly_income,
        subscription_length,
        monthly_bill,
        support_tickets,
        internet_usage,
        last_login,
        satisfaction_score
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer Will Churn")

    else:
        st.success("Customer Will Not Churn")