import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))

# Page title with styling
st.markdown(
    """
    <style>
        .title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: white;
        }
        .content {
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            backdrop-filter: blur(10px);
            padding: 20px;
            margin: 20px auto;
            width: 80%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Malaria Prediction using Machine Learning</div>', unsafe_allow_html=True)

# Container for input data
with st.container():
    st.markdown('<div class="content">', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Temperature_Above_Avg = st.text_input('Temperature Above Avg')
        
    with col2:
        High_Rainfall = st.text_input('High Rainfall')

    with col3:
        High_Humidity = st.text_input('High Humidity')
        
    with col4:
        High_Population_Density = st.text_input('High Population Density')
        
    with col5:
        Malaria_Outbreak = st.text_input('Malaria Outbreak')

    with col1:
        Insecticide_Use = st.text_input('Insecticide Use')
        
    with col2:
        Health_Facilities_Adequate = st.text_input('Health Facilities Adequate')

    with col3:
        Vaccination_Rate_High = st.text_input('Vaccination Rate High')
        
    with col4:
        Mosquito_Net_Coverage_High = st.text_input('Mosquito Net Coverage High')

    # Prediction
    Malaria_diagnosis = ''

    # Prediction button
    if st.button('🔍 Malaria Disease Test Button'):
        try:
            Malaria_disease_prediction = Malaria_Project.predict([[Temperature_Above_Avg, High_Rainfall, High_Humidity, High_Population_Density, Malaria_Outbreak, Insecticide_Use, Health_Facilities_Adequate, Vaccination_Rate_High, Mosquito_Net_Coverage_High]])
        except ValueError as e:
            st.error(f"Prediction error: {str(e)}")

        if Malaria_disease_prediction[0] == 1:
            Malaria_diagnosis = 'The person is affected with Malaria 😷'
        else:
            Malaria_diagnosis = 'The person is NOT affected with Malaria 😊'

    st.success(Malaria_diagnosis)

    st.markdown('</div>', unsafe_allow_html=True)
