import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load('model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

st.set_page_config(page_title="Finance Health Predictor", layout="centered")

st.title("💰 Financial Health Predictor")
st.markdown("Enter your income and spending details to get personalized financial advice.")

# Input fields
income = st.number_input("Monthly Income (₹)", min_value=1000, step=1000)
essential = st.number_input("Essential Spending (Rent, Food, Bills)", min_value=0, step=500)
discretionary = st.number_input("Discretionary Spending (Travel, Fun)", min_value=0, step=500)
savings = st.number_input("Monthly Savings", min_value=0, step=500)

# Predict button
if st.button("Predict Financial Health"):
    input_df = pd.DataFrame([{
        'income': income,
        'essential_spending': essential,
        'discretionary_spending': discretionary,
        'savings': savings
    }])
    
    pred = model.predict(input_df)[0]
    label = label_encoder.inverse_transform([pred])[0]

    if label == 'Healthy':
        advice = "✅ You're financially healthy. Keep saving and start investing long-term!"
    elif label == 'Moderate':
        advice = "⚠️ Moderate condition. Increase savings and reduce unnecessary expenses."
    else:
        advice = "🚨 Poor financial health. Reassess your budget and start saving more aggressively."

    st.subheader(f"Prediction: {label}")
    st.success(advice)
