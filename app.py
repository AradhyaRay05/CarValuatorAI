import streamlit as st
import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    best_catboost_model = pickle.load(f)
st.title('Car Price Prediction App')
st.write("""Enter the details of the car to predict its selling price.""")
present_price = st.slider('Present Price (in Lakhs)', 0.0, 35.0, 5.0) 
kms_driven = st.slider('Kilometers Driven', 0, 100000, 10000) 
owner = st.selectbox('Number of Owners', [0, 1, 2, 3])
no_year = st.slider('Number of Years Old', 0, 20, 5) 
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
if st.button('Predict Selling Price'):
    data = {
        'Present_Price': [present_price],
        'Kms_Driven': [kms_driven],
        'Owner': [owner],
        'no._year': [no_year],
        'Fuel_Type_Diesel': [fuel_type == 'Diesel'],
        'Fuel_Type_Petrol': [fuel_type == 'Petrol'],
        'Seller_Type_Individual': [seller_type == 'Individual'],
        'Transmission_Manual': [transmission == 'Manual']
    }
    input_df = pd.DataFrame(data)
    input_df = input_df[['Present_Price', 'Kms_Driven', 'Owner', 'no._year', 'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Seller_Type_Individual', 'Transmission_Manual']]
    prediction = best_catboost_model.predict(input_df)
    st.success(f'Predicted Selling Price: ₹ {prediction[0]:.2f} Lakhs')