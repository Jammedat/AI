import streamlit as st
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "nepali_news_classifier.joblib")
ENCODER_PATH = os.path.join(BASE_DIR, "nepali_news_label_encoder.joblib")

st.title("News category prediction")
input_text = st.text_input("Enter the news you want to predict")

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)  # load encoder

if st.button("PREDICT"):
    output = model.predict([input_text])
    category = label_encoder.inverse_transform(output)
    st.success(category[0])