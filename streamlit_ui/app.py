import streamlit as st
import requests

st.title("🩺 AI Medical Diagnostics Assistant")

symptom_input = st.text_area("Describe your symptoms")

if st.button("Get Diagnosis"):
    state_input = {
        "input": symptom_input,
        "symptom_area": "",
        "diagnosis": ""
    }

    try:
        response = requests.post(
            "https://medical-ai-p455.onrender.com/diagnose/invoke",
            headers={"Content-Type": "application/json"},
            json={"input": state_input}  
        )

        data = response.json()
        st.write("DEBUG Raw JSON:", data) 
        output_data = data.get("output", {})
        st.subheader("Symptom Area Detected:")
        st.write(output_data.get("symptom_area", "N/A"))

        st.subheader("AI Diagnosis Suggestion:")
        st.write(output_data.get("diagnosis", "N/A"))

    except Exception as e:
        st.error(f"Failed to get diagnosis: {e}")
