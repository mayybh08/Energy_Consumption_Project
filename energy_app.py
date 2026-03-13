#Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
import joblib as jb

st.title("---------Welcome to Energy Predictor Application--------")
data = pd.read_csv(r"C:\Users\MAYURI\Downloads\appliance_energy.csv")
st.write(data)
st.write("This is the Line Chart")
st.line_chart(data)



#Using the model
model = jb.load(r"C:\Users\MAYURI\Downloads\C__Users_MAYURI_OneDrive_Documents_Energy_Predictor.pkl")
temp = st.number_input("Enter the temperature:", min_value = 2.0, max_value = 50.0, value = 5.0)


#Converting input to numpy array
if st.button("Predict"):
    new_data = np.array([[temp]])
    prediction = model.predict(new_data)
    st.write(f"The predicted Energy Consumption is: {prediction[0]:.2f}")
    st.write("Thank You....!")