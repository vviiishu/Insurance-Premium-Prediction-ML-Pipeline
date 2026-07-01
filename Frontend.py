import os

import streamlit as st
import requests

# FastAPI Endpoint
# Defaults to localhost for local dev; override with API_URL env var in Docker
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000") + "/predict"

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered",
)

st.title("💰 Insurance Premium Category Predictor")
st.write("Fill in the details below to predict the insurance premium category.")

# --------------------------
# User Inputs
# --------------------------

age = st.number_input("Age", min_value=1, max_value=119, value=30)

weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)

height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.70)

income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)

smoker = st.selectbox("Smoker", [False, True])

city = st.text_input("City", value="Mumbai")

occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job",
    ],
)

# --------------------------
# Prediction Button
# --------------------------

if st.button("Predict Premium Category"):

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.success("Prediction Successful!")
            st.markdown("### Predicted Premium Category")
            st.info(result["predicted_category"])
            st.markdown("---")

            with st.expander("View API Response"):
                st.json(result)

        else:
            st.error(f"API returned Status Code: {response.status_code}")
            try:
                st.json(response.json())
            except Exception:
                st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("❌ Unable to connect to the FastAPI server.")
        st.info("Start the FastAPI server first using:")
        st.code("uvicorn app:app --reload")

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
