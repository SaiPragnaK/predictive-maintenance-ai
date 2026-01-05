import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Predictive Maintenance AI",
    page_icon="⚙️",
    layout="wide",
)

@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load("models/rf_model.joblib")
        scaler = joblib.load("models/scaler.joblib")
        feature_columns = joblib.load("models/feature_columns.joblib")
        return model, scaler, feature_columns
    except:
        return None, None, None

model, scaler, feature_columns = load_artifacts()

st.markdown("<h1 style='text-align: center;'>⚙️ Predictive Maintenance AI</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Predict machinery failure risk based on real-time sensor data.</p>",
    unsafe_allow_html=True
)
st.write("---")

if model is None or scaler is None:
    st.error("❌ Model files not found. Please run `train.py` first to generate model and scaler.")
else:

    st.subheader("📊 Enter Machine Sensor Readings")

    col1, col2 = st.columns(2)

    with col1:
        type_map = {'L': 0, 'M': 1, 'H': 2}
        machine_type = st.selectbox("Machine Type", list(type_map.keys()))
        air_temp = st.number_input("Air Temperature [K]", 290.0, 320.0, 298.0)
        process_temp = st.number_input("Process Temperature [K]", 300.0, 330.0, 308.0)

    with col2:
        rot_speed = st.number_input("Rotational Speed [rpm]", 1000.0, 3000.0, 1500.0)
        torque = st.number_input("Torque [Nm]", 0.0, 100.0, 40.0)
        tool_wear = st.number_input("Tool Wear [min]", 0.0, 250.0, 50.0)

    if st.button("🔍 Analyze Failure Risk", use_container_width=True, type="primary"):
        input_df = pd.DataFrame([{
            'Type': type_map[machine_type],
            'Air temperature [K]': air_temp,
            'Process temperature [K]': process_temp,
            'Rotational speed [rpm]': rot_speed,
            'Torque [Nm]': torque,
            'Tool wear [min]': tool_wear
        }])

        try:
            scaled_data = scaler.transform(input_df)
            prediction = model.predict(scaled_data)[0]

            st.write("---")
            st.subheader("📈 Prediction Result")

            if prediction == 1:
                st.error(
                    "⚠️ **High Failure Risk Detected!**",
                    icon="🚨"
                )
                st.info("🛠️ Schedule maintenance immediately to avoid downtime.")
            else:
                st.success(
                    "✅ **Machine Operating Normally**",
                    icon="👍"
                )
                st.info("🟢 The machine is running within safe operational limits.")

        except Exception as e:
            st.error(f"Error during prediction: {e}")

st.write("---")
st.caption("Developed using AI4I 2020 Predictive Maintenance Dataset.")
