import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
malaria = pickle.load(open('malaria_model.sav', 'rb'))

# Apply custom CSS for background and styling
page_bg_img = '''
<style>
    body {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/pexels-slendyalex-3941855.jpg?raw=true");
        background-size: cover;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Page title
st.title('🌿 Malaria Prediction using Machine Learning')

# Input data section with columns
st.subheader("Enter Health and Environmental Factors")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    temperature_above_avg = st.text_input('🌡 Temperature Above Avg')

with col2:
    high_rainfall = st.text_input('🌧 High Rainfall')

with col3:
    high_humidity = st.text_input('💧 High Humidity')

with col4:
    high_population_density = st.text_input('🏙 Population Density')

with col5:
    malaria_outbreak = st.text_input('🦟 Malaria Outbreak')

with col1:
    health_facilities_adequate = st.text_input('🏥 Health Facilities Adequate')

with col2:
    vaccination_rate_high = st.text_input('💉 Vaccination Rate High')

with col3:
    mosquito_net_coverage_high = st.text_input('🛏 Mosquito Net Coverage High')

# Prediction result
malaria_diagnosis = ''

# Prediction button with improved styling
if st.button('🔍 Predict Malaria'):
    malaria_prediction = malaria.predict([[temperature_above_avg, high_rainfall, high_humidity, 
                                           high_population_density, malaria_outbreak, 
                                           health_facilities_adequate, vaccination_rate_high, 
                                           mosquito_net_coverage_high]])

    if malaria_prediction[0] == 1:
        malaria_diagnosis = 'The person is affected with Malaria 😷'
    else:
        malaria_diagnosis = 'The person is NOT affected with Malaria 😊'

# Display the diagnosis result
st.success(malaria_diagnosis)
