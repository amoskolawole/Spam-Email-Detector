import streamlit as st
import joblib

# Load saved files
model = joblib.load("Spam_Detection_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App title
st.title("📧 Spam Message Detector")

# User input
message = st.text_area("Enter a message")

# Predict button
if st.button("Predict"):

    # Transform message
    message_vector = vectorizer.transform([message])

    # Predict
    prediction = model.predict(message_vector)

    # Display result
    if prediction[0] == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Ham (Normal Message)")
