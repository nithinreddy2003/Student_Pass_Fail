
# ============================================
# Create Streamlit App
# ============================================

import streamlit as st
import pandas as pd
import pickle

# Load saved model
with open("sony_padhu.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Pass / Fail Prediction")

st.write("Enter the student's marks below.")

# Input fields
quiz1 = st.number_input(
    "Quiz 1 Marks",
    min_value=0.0,
    max_value=10.0,
    value=5.0
)

quiz2 = st.number_input(
    "Quiz 2 Marks",
    min_value=0.0,
    max_value=10.0,
    value=5.0
)

assignment1 = st.number_input(
    "Assignment 1 Marks",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

assignment2 = st.number_input(
    "Assignment 2 Marks",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

# Prediction
if st.button("Predict Result"):

    input_data = pd.DataFrame(
        [[quiz1, quiz2, assignment1, assignment2]],
        columns=[
            "Quiz1",
            "Quiz2",
            "Assignment1",
            "Assignment2"
        ]
    )

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.success("PASS")
    else:
        st.error("FAIL")

    st.write(f"Probability of Passing: {probability:.2%}")
