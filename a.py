import joblib
import streamlit as st

import pandas as pd

model = joblib.load('mj')
st.title("HOUSE PRICE PREDICTION")

# def  prediction(area):
#     prediction = model.predict([[area]])
#     return prediction

area = st.number_input("Enter The Area")
# bedroom = st.number_input("Enter the Bedroom")

def prediction(area):
    p = model.predict([[area]])
    return p

if(st.button("Predict")):
    result = prediction(area)
    st.success('The Predicted Price is {}'.format(result))