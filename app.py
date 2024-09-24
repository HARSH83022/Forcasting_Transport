import streamlit as st
import joblib
import pandas as pd

# Load the model binary file
model = joblib.load('transportation_demand.pkl')

# Creating App
st.title('Transportation Demand Predictor')

# Input fields
population_density = st.number_input('Population Density (people/km²)')
gdp_per_capita = st.number_input('GDP Per Capita ($)')
employment_rate = st.number_input('Employment Rate (%)')
public_transit_availability = st.selectbox('Public Transit Availability', [0, 1])
ridesharing_availability = st.selectbox('Ridesharing Availability', [0, 1])
historical_public_transit_usage = st.number_input('Historical Public Transit Usage')
historical_ridesharing_usage = st.number_input('Historical Ridesharing Usage')
event_occurrence = st.number_input('Event Occurrence (0 or 1)')

# Creating input DataFrame
input_data = pd.DataFrame({
    'Population_Density': [population_density],
    'GDP_Per_Capita': [gdp_per_capita],
    'Employment_Rate': [employment_rate],
    'Public_Transit_Availability': [public_transit_availability],
    'Ridesharing_Availability': [ridesharing_availability],
    'Historical_Public_Transit_Usage': [historical_public_transit_usage],
    'Historical_Ridesharing_Usage': [historical_ridesharing_usage],
    'Event_Occurrence': [event_occurrence]
})

# Prediction button
if st.button('Predict'):
    demand_prediction = model.predict(input_data)
    st.write(f'Predicted Demand: {demand_prediction[0]}')
