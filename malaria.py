import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
malaria = pickle.load(open('malaria_model10.sav', 'rb'))

# Use the raw GitHub link for the background image
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://th.bing.com/th/id/OIP.TVtx79z6Rt6kX0ei9yRdJwHaEJ?rs=1&pid=ImgDetMain");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); /* Transparent header */
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
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Page title
st.title('🌿 Malaria Prediction using Machine Learning')

# Input section
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
