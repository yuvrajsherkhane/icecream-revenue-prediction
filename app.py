import streamlit as st
import joblib
model=joblib.load("Revenue.pkl")
st.title("Cold Stone")
st.header("Revenue Prediction")
temp=st.number_input("Enter the Temperature")
if st.button("Predict"):
    st.write(model.predict([[temp]]))
