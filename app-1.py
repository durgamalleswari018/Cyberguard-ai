import streamlit as st
import pandas as pd
import joblib

model = joblib.load("cyberguard_ai_model.pkl")

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberGuard AI")
st.subheader("AI-Powered Network Intrusion Detection")

st.write("Enter network traffic feature values to detect potential threats.")

values = {}

for feature in model.feature_names_in_:
    values[feature] = st.number_input(feature, value=0.0)

if st.button("🔍 Detect Traffic"):
    data = pd.DataFrame([values])
    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("🚨 ATTACK DETECTED")
    else:
        st.success("✅ NORMAL TRAFFIC")

st.divider()
st.caption("CyberGuard AI | Machine Learning + Cybersecurity")
