import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

malaria = pickle.load(open('malaria_model.sav', 'rb'))
# page title
st.title('Malaria Prediction using ML')


# getting the input data from the user
col1, col2, col3,col4, col5 = st.columns(5)

with col1:
    Diagnosis = st.text_input('Region')
    
with col2:
    Radius_mean = st.text_input('Year')

with col3:
    Texture_mean = st.text_input('Month')
    
with col4:
    Perimeter_mean = st.text_input('Temperature Above Avg')
    
with col5:
    Area_mean = st.text_input('High_Rainfall')

with col1:
    Smoothness_mean = st.text_input('High_Humidity')
    
with col2:
    Compactness_mean = st.text_input('High_Population_Density')

with col3:
    Contactivity_mean = st.text_input('Malaria_Outbreak')
    
with col4:
    Concave_points_mean = st.text_input('Health_Facilities_Adequate')
  
with col5:
    Area_mean = st.text_input('Vaccination_Rate_High')

with col1:
    Smoothness_mean = st.text_input('Mosquito_Net_Coverage_High')


# code for Prediction
malaria_diagnosis = ''

# creating a button for Prediction

if st.button('Malaria Test Button'):
    malaria_prediction = malaria.predict([[]])
    
    if (malaria_prediction[0] == 1):
      malaria_diagnosis = 'The person is Effected with Malaria'
    else:
      malaria_diagnosis = 'The person is NOT Effected with Malaria'
    
st.success(malaria_diagnosis)
