import streamlit as st
import pickle
import numpy as np

# Load model
data = pickle.load(open("svm_model.pkl", "rb"))

model = data["model"]

st.title("SVM Prediction App")

st.write("Enter values below")

# Example input fields
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")
feature4 = st.number_input("Feature 4")

if st.button("Predict"):

    input_data = np.array([
        [feature1, feature2, feature3, feature4]
    ])

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")