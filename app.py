
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Electricity Bill Predictor",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Electricity Bill Prediction")
st.write("Predict your electricity bill based on AC consumption units.")

@st.cache_resource
def load_model():
    return joblib.load("electric_bill_model.pkl")

model = load_model()

st.subheader("Enter AC Consumption")

ac_units = st.number_input(
    "AC Units",
    value=1,
    step=1
)

if st.button("Predict Electricity Bill"):

    if ac_units <= 0:
        st.toast("⚠️ Value must be greater than 0!", icon="⚠️")
        st.error("Please enter value greater than 0.")

    elif ac_units > 150:
        st.toast("⚠️ Value should not exceed 150!", icon="⚠️")
        st.error("Please enter value less than or equal to 150.")

    else:
        new_data = pd.DataFrame({
            "AC_Units": [ac_units]
        })

        predicted_bill = model.predict(new_data)[0]

        st.success(
            f"Predicted Electricity Bill: ₹{predicted_bill:.2f}"
        )
