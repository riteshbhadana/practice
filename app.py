import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("Salary Prediction App")

exp = st.number_input("Years of Experience")

if st.button("Predict"):
    pred = model.predict([[exp]])
    st.write("Salary =", pred)