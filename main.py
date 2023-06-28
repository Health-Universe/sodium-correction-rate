import streamlit as st
import math

def calculate_correction(current_sodium, desired_sodium, weight, time):
    if current_sodium < desired_sodium:  # hyponatremia
        correction_rate = (desired_sodium - current_sodium) / time
        sodium_infusion_rate = 0.6 * weight * correction_rate
    else:  # hypernatremia
        correction_rate = (current_sodium - desired_sodium) / time
        sodium_infusion_rate = -1 * (0.6 * weight * correction_rate)

    return correction_rate, sodium_infusion_rate

st.title("Sodium Correction Rate Calculator")
st.write("""
This app calculates the sodium correction rate for hyponatremia or hypernatremia.
Please input the patient's details below.
""")

current_sodium = st.number_input("Current sodium level (mEq/L)", min_value=0, max_value=200)
desired_sodium = st.number_input("Desired sodium level (mEq/L)", min_value=0, max_value=200)
weight = st.number_input("Patient weight (kg)", min_value=0, max_value=300)
time = st.number_input("Desired time for correction (hours)", min_value=0, max_value=72)

if st.button("Calculate"):
    correction_rate, infusion_rate = calculate_correction(current_sodium, desired_sodium, weight, time)
    st.write(f"The correction rate is {correction_rate} mEq/L/h.")
    st.write(f"The sodium infusion rate is {infusion_rate} mL/h.")
