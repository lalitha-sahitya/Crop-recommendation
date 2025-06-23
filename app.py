import streamlit as st
import pandas as pd
import numpy as np
import pickle
with open('model (2).pkl', 'rb') as f:
    loaded_model = pickle.load(f)
st.title('Crop recommendation 🌾')
N = st.number_input('Nitrogen content (N)', min_value=0, max_value=250)
P = st.number_input('Phosphorus content (P)', min_value=0, max_value=250)
K = st.number_input('Potassium content (K)', min_value=0, max_value=250)
temperature = st.slider(
    'Select temperature (°C)',
    min_value=5,
    max_value=50,
    value=25
)
humidity = st.slider('Humidity (%)', min_value=10, max_value=100, value=50)
rainfall = st.slider('Rainfall (mm)', min_value=20, max_value=300, value=100)
ph = st.slider('pH', min_value=3.5, max_value=9.5, value=6.5, step=0.1)
labels = [
    "apple", "banana", "blackgram", "chickpea", "coconut", "coffee", "cotton",
    "grapes", "jute", "kidneybeans", "lentil", "maize", "mango", "mothbeans",
    "mungbean", "muskmelon", "orange", "papaya", "pigeonpeas", "pomegranate",
    "rice", "watermelon"
]
if st.button('Recommend'):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = loaded_model.predict(input_data)
    predicted_crop = labels[int(prediction[0])]
    st.success(f"The recommended crop is: **{predicted_crop.capitalize()}**")