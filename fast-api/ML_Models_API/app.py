import streamlit as st
import requests


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ML Prediction App",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🤖 ML Prediction System")
st.write("Enter the user information below to get a prediction.")


# FastAPI URL
API_URL = "http://127.0.0.1:8000/predict"


# -----------------------------
# Input Form
# -----------------------------
with st.form("prediction_form"):

    st.subheader("User Information")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=99,
        value=25
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.1,
        max_value=199.9,
        value=70.0
    )

    height = st.number_input(
        "Height (meters)",
        min_value=0.1,
        max_value=2.99,
        value=1.70,
        step=0.01
    )

    income_lpa = st.number_input(
        "Income (LPA)",
        min_value=0.1,
        value=5.0,
        step=0.1
    )

    smoker = st.selectbox(
        "Smoker",
        options=[False, True],
        format_func=lambda x: "Yes" if x else "No"
    )

    city = st.text_input(
        "City",
        value="Mumbai"
    )

    occupation = st.selectbox(
        "Occupation",
        options=[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job"
        ]
    )

    submitted = st.form_submit_button(
        "🔮 Predict",
        use_container_width=True
    )


# -----------------------------
# Prediction
# -----------------------------
if submitted:

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:

        response = requests.post(
            API_URL,
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction successful! 🎉")

            prediction = result["predicted_category"]

            st.subheader("Prediction Result")

            st.info(
                f"Predicted Category: **{prediction}**"
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to FastAPI."
        )

        st.info(
            "Make sure your FastAPI server is running."
        )