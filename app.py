import streamlit as st
import joblib

# Load model
model = joblib.load("model/phishing_model.pkl")

st.title("Phishing Email Detector")
st.write("Paste an email below to check if it's a phishing attempt:")

email_input = st.text_area("Email Content", height=200)

if st.button("Analyze"):
    if email_input.strip() == "":
        st.warning("Please enter some email content.")
    else:
        prediction = model.predict([email_input])[0]
        probability = model.predict_proba([email_input])[0]

        if prediction == 1:
            st.error(f"Phishing detected: ({probability[1]:.0%} confidence)")
        else:
            st.success(f"Looks safe: ({probability[0]:.0%} confidence)")
