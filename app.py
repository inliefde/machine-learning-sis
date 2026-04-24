import streamlit as st
import requests

st.set_page_config(page_title="Inliefde Wine Predict System", layout="centered")

st.title("🍷 Inliefde Wine Predict System")
st.write("Enter the wine features below to predict its class.")

with st.form("wine_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        alcohol = st.number_input("Alcohol", value=13.0, step=0.1)
        malic_acid = st.number_input("Malic Acid", value=2.0, step=0.1)
        ash = st.number_input("Ash", value=2.3, step=0.1)
        alcalinity_of_ash = st.number_input("Alcalinity of Ash", value=19.5, step=0.1)
        magnesium = st.number_input("Magnesium", value=100.0, step=1.0)
        total_phenols = st.number_input("Total Phenols", value=2.2, step=0.1)
        flavanoids = st.number_input("Flavanoids", value=2.0, step=0.1)
        
    with col2:
        nonflavanoid_phenols = st.number_input("Nonflavanoid Phenols", value=0.3, step=0.01)
        proanthocyanins = st.number_input("Proanthocyanins", value=1.5, step=0.1)
        color_intensity = st.number_input("Color Intensity", value=4.5, step=0.1)
        hue = st.number_input("Hue", value=1.0, step=0.01)
        od280_od315_of_diluted_wines = st.number_input("OD280/OD315", value=2.6, step=0.1)
        proline = st.number_input("Proline", value=750.0, step=10.0)


    submitted = st.form_submit_button("Predict")

if submitted:
   
    payload = {
        "alcohol": float(alcohol),
        "malic_acid": float(malic_acid),
        "ash": float(ash),
        "alcalinity_of_ash": float(alcalinity_of_ash),
        "magnesium": float(magnesium),
        "total_phenols": float(total_phenols),
        "flavanoids": float(flavanoids),
        "nonflavanoid_phenols": float(nonflavanoid_phenols),
        "proanthocyanins": float(proanthocyanins),
        "color_intensity": float(color_intensity),
        "hue": float(hue),
        "od280_od315_of_diluted_wines": float(od280_od315_of_diluted_wines),
        "proline": float(proline)
    }


    try:
        response = requests.post("http://api:8000/predict", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            st.success(f"Prediction: {data.get('predicted_class')} (Class {data.get('prediction')})")
        else:
            st.error(f"Error from API: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to API. Is FastAPI running on http://api:8000?")
