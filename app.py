import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
data = pickle.load(open("svm_model.pkl", "rb"))

model = data["model"]

st.title("Customer Churn Prediction using SVM")

# Inputs
age = st.number_input("Age")

monthly_income = st.number_input("Monthly Income")

subscription_length = st.number_input(
    "Subscription Length Months"
)

monthly_bill = st.number_input("Monthly Bill")

support_tickets = st.number_input("Support Tickets")

internet_usage = st.number_input("Internet Usage GB")

last_login = st.number_input("Last Login Days Ago")

satisfaction_score = st.number_input("Satisfaction Score")

if st.button("Predict"):

    input_df = pd.DataFrame([{
        "Age": age,
        "Monthly_Income": monthly_income,
        "Subscription_Length_Months": subscription_length,
        "Monthly_Bill": monthly_bill,
        "Support_Tickets": support_tickets,
        "Internet_Usage_GB": internet_usage,
        "Last_Login_Days_Ago": last_login,
        "Satisfaction_Score": satisfaction_score
    }])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Customer Will Churn")

    else:
        st.success("Customer Will Not Churn")