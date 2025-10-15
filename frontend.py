import streamlit as st
import requests

# -----------------------------
# Page Config
st.set_page_config(page_title="Text Classifier AI", layout="centered")
st.title("📝 Text Classifier AI")
st.write("Enter a text below and see which category it belongs to.")

# -----------------------------
# User Input
user_text = st.text_area("Type your text here:")

# -----------------------------
# Predict Button
if st.button("Predict"):
    if user_text.strip() == "":
        st.warning("Please enter some text before predicting.")
    else:
        # Call Flask API
        try:
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"text": user_text}
            )
            if response.status_code == 200:
                result = response.json()
                st.success("Prediction successful!")
                st.write("**Text:**", result["text"])
                st.write("**Category:**", result["category"])
            else:
                st.error(f"API returned an error: {response.status_code}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")


