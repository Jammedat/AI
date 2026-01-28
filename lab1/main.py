import streamlit as st
import joblib
 
model = joblib.load('knn_model.joblib')
st.title("Titanic Survivors Prediction")

PassengerId = st.number_input(label="Passenger Id", min_value=1, max_value=891, value=21)
Pclass = st.number_input(label="Passenger Class", min_value=1, max_value=3, value=2)
Sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "male" if x==0 else "female")

Age = st.number_input(label="Age", min_value=1, max_value=100, value=35)
SibSp = st.number_input("No. of siblings or spouses aboard the titanic")
Parch = st.number_input("No. of parents or children aboard the titanic")
Fare = st.number_input("Fare")
Embarked = st.selectbox("Embarked", options=[0, 1, 2], format_func=lambda x: "C" if x==0 else "Q" if x==1 else "S")
sample=[[PassengerId, Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]

if st.button("Predict"):
    prediction = model.predict(sample)[0]
    result = "Survived" if prediction == 1 else "did not Survive"
    st.success(f"Predicted passenger {result}")





