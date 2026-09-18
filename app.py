
import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Electricity Bill Predictor",
    page_icon="⚡",
    layout="centered"
)

# Title
st.title("⚡ Electricity Bill Prediction")
st.write(
    "Predict your electricity bill based on AC consumption units "
    "using Polynomial Regression."
)

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("electric_bill_model.pkl")

try:
    model = load_model()

    st.subheader("Enter AC Consumption")

    ac_units = st.number_input(
        "AC Units",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    if st.button("Predict Electricity Bill"):
        new_data = pd.DataFrame({
            "AC_Units": [ac_units]
        })

        predicted_bill = model.predict(new_data)[0]

        st.success(
            f"Predicted Electricity Bill: ₹{predicted_bill:.2f}"
        )

except FileNotFoundError:
    st.error(
        "Model file not found. Please place "
        "'electric_bill_model.pkl' in the same folder as app.py."
    )

except Exception as e:
    st.error(f"An error occurred: {e}")
