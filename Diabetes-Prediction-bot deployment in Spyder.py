# Import necessary libraries
import pickle
import streamlit as st

# Load the diabetes model
diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))

# Create a Streamlit app for Diabetes Prediction
st.title('Diabetes Prediction using ML')

# Input fields
Pregnancies = st.text_input('Number of Pregnancies')
Glucose = st.text_input('Glucose Level')
BloodPressure = st.text_input('Blood Pressure value')
SkinThickness = st.text_input('Skin Thickness value')
Insulin = st.text_input('Insulin Level')
BMI = st.text_input('BMI value')
DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
Age = st.text_input('Age of the Person')

# Prediction logic
diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'
st.success(diab_diagnosis)
