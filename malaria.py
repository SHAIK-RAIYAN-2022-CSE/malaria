import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
malaria = pickle.load(open('malaria_model10.sav', 'rb'))

# Use the raw GitHub link for the background image
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); /* Transparent header */
    }
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 8px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
    }
    .block-container {
        padding-top: 2rem;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Page title
st.title('🌿 Malaria Prediction using Machine Learning')

# Input section
st.subheader("Enter Health and Environmental Factors")

# Create three rows for alignment
with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        temperature_above_avg = st.text_input('🌡 Temperature Above Avg')
        health_facilities_adequate = st.text_input('🏥 Health Facilities Adequate')

    with col2:
        high_rainfall = st.text_input('🌧 High Rainfall')
        vaccination_rate_high = st.text_input('💉 Vaccination Rate High')

    with col3:
        high_humidity = st.text_input('💧 High Humidity')
        mosquito_net_coverage_high = st.text_input('🛏 Mosquito Net Coverage High')

    with col4:
        high_population_density = st.text_input('🏙 Population Density')
        malaria_outbreak = st.text_input('🦟 Malaria Outbreak')

# Prediction result
malaria_diagnosis = ''

# Prediction button
if st.button('🔍 Predict Malaria'):
    malaria_prediction = malaria.predict([[temperature_above_avg, high_rainfall, high_humidity,
                                           high_population_density, malaria_outbreak,
                                           health_facilities_adequate, vaccination_rate_high,
                                           mosquito_net_coverage_high]])

    if malaria_prediction[0] == 1:
        malaria_diagnosis = 'The person is affected with Malaria 😷'
    else:
        malaria_diagnosis = 'The person is NOT affected with Malaria 😊'

# Display result
st.success(malaria_diagnosis)
