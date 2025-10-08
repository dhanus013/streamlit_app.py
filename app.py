# ==============================
# 🔹 Loading the required libraries
# ==============================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # ✅ Use joblib instead of pickle

# ==============================
# 🔹 Load the model using joblib
# ==============================
classifier = joblib.load('log_model.pkl')  # or logisticRegr.joblib if you saved with that name

# ==============================
# 🔹 Streamlit App UI
# ==============================
st.sidebar.header('Diabetes Prediction')
select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')

if not st.sidebar.checkbox("Hide", True, key='2'):
    st.title('Diabetes Prediction (Only for females above 21 years of age)')
    
    name = st.text_input("Name:")
    pregnancy = st.number_input("No. of times pregnant:")
    glucose = st.number_input("Plasma Glucose Concentration:")
    bp = st.number_input("Diastolic blood pressure (mm Hg):")
    skin = st.number_input("Triceps skin fold thickness (mm):")
    insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
    dpf = st.number_input("Diabetes Pedigree Function:")
    age = st.number_input("Age:")
    
    submit = st.button('Predict')
    
    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.success(f'🎉 Congratulations {name}, you are **not diabetic**.')
        else:
            st.error(f"⚠️ {name}, we are really sorry to say but it seems like you are **diabetic**.")
