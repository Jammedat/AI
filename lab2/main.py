import streamlit as st
import joblib

st.title("News category prediction")
input_text = st.text_input("Enter the news you want to predict")

model = joblib.load("nepali_news_classifier.joblib")
label_encoder = joblib.load("nepali_news_label_encoder.joblib")  # load encoder

if st.button("PREDICT"):
    output = model.predict([input_text])
    category = label_encoder.inverse_transform(output)
    st.success(category[0])