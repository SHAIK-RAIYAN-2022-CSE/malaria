import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
malaria = pickle.load(open('malaria_model.sav', 'rb'))

# Page title
st.title('Malaria Prediction using ML')

# Input data
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    region = st.text_input('Region')

with col2:
    year = st.text_input('Year')

with col3:
    month = st.text_input('Month')

with col4:
    temperature_above_avg = st.text_input('Temperature Above Avg')

with col5:
    high_rainfall = st.text_input('High Rainfall')

with col1:
    high_humidity = st.text_input('High Humidity')

with col2:
    high_population_density = st.text_input('High Population Density')

with col3:
    malaria_outbreak = st.text_input('Malaria Outbreak')

with col4:
    health_facilities_adequate = st.text_input('Health Facilities Adequate')

with col5:
    vaccination_rate_high = st.text_input('Vaccination Rate High')

with col1:
    mosquito_net_coverage_high = st.text_input('Mosquito Net Coverage High')

# Prediction result
malaria_diagnosis = ''

# Prediction button
if st.button('Malaria Test Button'):
    malaria_prediction = malaria.predict([[temperature_above_avg, high_rainfall, high_humidity, high_population_density, malaria_outbreak, health_facilities_adequate, vaccination_rate_high, mosquito_net_coverage_high]])

    if malaria_prediction[0] == 1:
        malaria_diagnosis = 'The person is affected with Malaria'
    else:
        malaria_diagnosis = 'The person is NOT affected with Malaria'

st.success(malaria_diagnosis)
