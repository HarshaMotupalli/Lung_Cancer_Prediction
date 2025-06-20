import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("lung_model.pkl")

st.set_page_config(page_title="Lung Cancer Prediction", layout="centered")

st.title("🔬 Lung Cancer Prediction App")
st.write("Enter patient information below:")

# Input fields
gender = st.selectbox("Gender", ["Female", "Male"])
gender = 0 if gender == "Female" else 1

age = st.slider("Age (normalized 0–1)", 0.0, 1.0, 0.5)

smoking = st.selectbox("Smoking", ["No", "Yes"])
yellow_fingers = st.selectbox("Yellow Fingers", ["No", "Yes"])
anxiety = st.selectbox("Anxiety", ["No", "Yes"])
peer_pressure = st.selectbox("Peer Pressure", ["No", "Yes"])
chronic_disease = st.selectbox("Chronic Disease", ["No", "Yes"])
fatigue = st.selectbox("Fatigue", ["No", "Yes"])
allergy = st.selectbox("Allergy", ["No", "Yes"])
wheezing = st.selectbox("Wheezing", ["No", "Yes"])
alcohol = st.selectbox("Alcohol Consuming", ["No", "Yes"])
coughing = st.selectbox("Coughing", ["No", "Yes"])
shortness_of_breath = st.selectbox("Shortness of Breath", ["No", "Yes"])
swallowing_difficulty = st.selectbox("Swallowing Difficulty", ["No", "Yes"])
chest_pain = st.selectbox("Chest Pain", ["No", "Yes"])

# Map Yes/No to 1/0
def yes_no(val): return 1 if val == "Yes" else 0

features = np.array([[gender, age,
                      yes_no(smoking),
                      yes_no(yellow_fingers),
                      yes_no(anxiety),
                      yes_no(peer_pressure),
                      yes_no(chronic_disease),
                      yes_no(fatigue),
                      yes_no(allergy),
                      yes_no(wheezing),
                      yes_no(alcohol),
                      yes_no(coughing),
                      yes_no(shortness_of_breath),
                      yes_no(swallowing_difficulty),
                      yes_no(chest_pain)]])

# Predict
if st.button("🔍 Predict"):
    prediction = model.predict(features)[0]
    st.subheader("🎯 Prediction:")
    st.success("✅ LUNG CANCER DETECTED" if prediction == 1 else "❌ NO LUNG CANCER DETECTED")
    st.write("Thank you for using the Lung Cancer Prediction App!")