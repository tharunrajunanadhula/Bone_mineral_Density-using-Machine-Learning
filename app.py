import streamlit as st
import pickle
import pandas as pd

with open("BMD_RG.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Bone Mineral Density Prediction")

age = st.slider("Age", 18, 89, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", 15.0, 46.49, 22.0)
activity = st.number_input("Physical Activity", 0, 599, 30)
calcium = st.number_input("Calcium Intake", 400, 2000, 800)
smoking = st.selectbox("Smoking Status", ["Never", "Former"])
alcohol = st.selectbox("Alcohol Consumption", ["No", "Moderate"])

data = pd.DataFrame([{
    "Age": age,
    "Gender": gender,
    "BMI": bmi,
    "Physical_Activity_Min": activity,
    "Calcium_Intake_mg": calcium,
    "Smoking_Status": smoking,
    "Alcohol_Consumption": alcohol
}])

if st.button("Predict"):
    pred = model.predict(data)[0]
    st.success(f"Predicted BMD: {pred:.3f}")
