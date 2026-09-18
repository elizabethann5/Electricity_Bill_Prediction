
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Electricity Bill Predictor",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Electricity Bill Prediction")

st.write(
    "Predict your electricity bill using AC and fan consumption."
)

@st.cache_resource
def load_model():
    return joblib.load("electric_bill_model.pkl")

model = load_model()

st.subheader("Enter Consumption Details")

ac_units = st.number_input(
    "AC Units",
    min_value=0.0,
    value=1.0,
    step=1.0
)

fan_units = st.number_input(
    "Fan Units",
    min_value=0.0,
    value=1.0,
    step=1.0
)

if st.button("Predict Electricity Bill"):

    if ac_units <= 0 or fan_units <= 0:
        st.error("Both values must be greater than 0.")

    else:
        new_data = pd.DataFrame({
            "AC_Units": [ac_units],
            "Fan_Units": [fan_units]
        })

        prediction = model.predict(new_data)[0]

        st.success(
            f"Predicted Electricity Bill: ₹{prediction:.2f}"
        )
