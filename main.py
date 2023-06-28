import streamlit as st
import math

def calculate_correction(current_sodium, desired_sodium, weight, time, sodium_concentration):
    if current_sodium < desired_sodium:  # hyponatremia
        correction_rate = (desired_sodium - current_sodium) / time
        sodium_infusion_rate = 0.6 * weight * correction_rate
    else:  # hypernatremia
        correction_rate = (current_sodium - desired_sodium) / time
        sodium_infusion_rate = -1 * (0.6 * weight * correction_rate)

    # Adjust infusion rate based on sodium concentration
    sodium_infusion_rate = sodium_infusion_rate / sodium_concentration

    return correction_rate, sodium_infusion_rate

st.title("Sodium Correction Rate Calculator")
st.write("""
This app calculates the sodium correction rate for hyponatremia or hypernatremia.
Please input the patient's details below.
""")

current_sodium = st.number_input("Current sodium level (mEq/L) (Normal: 135-145 mEq/L)", min_value=0, max_value=200)
desired_sodium = st.number_input("Desired sodium level (mEq/L) (Normal: 135-145 mEq/L)", min_value=0, max_value=200)
weight = st.number_input("Patient weight (kg)", min_value=0, max_value=300)
time = st.number_input("Desired time for correction (hours) (Typically: 24-48 hours)", min_value=0, max_value=72)
sodium_concentration = st.selectbox("Sodium infusion concentration (%)", options=[0.9, 3])

if st.button("Calculate"):
    correction_rate, infusion_rate = calculate_correction(current_sodium, desired_sodium, weight, time, sodium_concentration)
    st.write(f"The correction rate is {correction_rate} mEq/L/h.")
    st.write(f"The sodium infusion rate is {infusion_rate} mL/h.")
