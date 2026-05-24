import streamlit as st
import joblib
import pandas as pd

# LOAD MODEL
model = joblib.load("accident_model.pkl")

# PAGE TITLE
st.title("Road Accident Severity Prediction")

st.write("Enter accident details below")

# INPUTS

traffic_control_device = st.selectbox(
    "Traffic Control Device",
    ["TRAFFIC SIGNAL", "STOP SIGN", "NO CONTROLS"]
)

weather_condition = st.selectbox(
    "Weather Condition",
    ["CLEAR", "RAIN", "SNOW", "FOG"]
)

lighting_condition = st.selectbox(
    "Lighting Condition",
    ["DAYLIGHT", "DARKNESS", "DUSK"]
)

first_crash_type = st.selectbox(
    "First Crash Type",
    ["REAR END", "ANGLE", "SIDESWIPE"]
)

trafficway_type = st.selectbox(
    "Trafficway Type",
    ["ONE-WAY", "TWO-WAY"]
)

alignment = st.selectbox(
    "Road Alignment",
    ["STRAIGHT", "CURVE"]
)

roadway_surface_cond = st.selectbox(
    "Road Surface Condition",
    ["DRY", "WET", "SNOW"]
)

road_defect = st.selectbox(
    "Road Defect",
    ["NO DEFECTS", "POTHOLES"]
)

crash_hour = st.slider(
    "Crash Hour",
    0,
    23
)

crash_day_of_week = st.slider(
    "Crash Day Of Week",
    1,
    7
)

# SIMPLE MANUAL ENCODING

data = {

    'traffic_control_device': 0,
    'weather_condition': 0,
    'lighting_condition': 0,
    'first_crash_type': 0,
    'trafficway_type': 0,
    'alignment': 0,
    'roadway_surface_cond': 0,
    'road_defect': 0,
    'crash_hour': crash_hour,
    'crash_day_of_week': crash_day_of_week

}

# CREATE DATAFRAME

input_data = pd.DataFrame([data])

# PREDICTION BUTTON

if st.button("Predict Accident Severity"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Crash Type: {prediction[0]}")
