import streamlit as st
import numpy as np
import pickle

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered",
)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    with open(r"C:\Users\npal1\Desktop\Nikhil\coding\Streamlit\medical_insurance_prediction\medical_insurance_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏥 Medical Insurance Cost Predictor")
st.markdown(
    "Fill in the details below to get an **estimated insurance charge** "
    "based on a Linear Regression model trained on the insurance dataset."
)
st.divider()

# ── Input form ────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age", min_value=18, max_value=100, value=31, step=1,
        help="Age of the primary beneficiary"
    )

    sex = st.selectbox(
        "Sex", options=["Male", "Female"],
        help="Gender of the policy holder"
    )

    bmi = st.number_input(
        "BMI", min_value=10.0, max_value=60.0, value=25.74, step=0.01,
        help="Body Mass Index. Normal range: 18.5 – 24.9"
    )

with col2:
    children = st.number_input(
        "Number of Children", min_value=0, max_value=10, value=0, step=1,
        help="Number of dependents covered by insurance"
    )

    smoker = st.selectbox(
        "Smoker", options=["Yes", "No"],
        help="Does the beneficiary smoke?"
    )

    region = st.selectbox(
        "Region", options=["Southeast", "Southwest", "Northeast", "Northwest"],
        help="Residential area in the US"
    )

st.divider()

# ── Encoding (mirrors notebook preprocessing) ─────────────────────────────────
sex_enc     = 0 if sex == "Male" else 1          # male=0, female=1
smoker_enc  = 0 if smoker == "Yes" else 1        # yes=0,  no=1
region_map  = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}
region_enc  = region_map[region]

# ── Prediction ────────────────────────────────────────────────────────────────
if st.button("💰 Predict Insurance Cost", use_container_width=True):
    input_data = np.asarray(
        [age, sex_enc, bmi, children, smoker_enc, region_enc]
    ).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"### Estimated Insurance Charge: **${prediction:,.2f}**")

    # Extra context cards
    c1, c2, c3 = st.columns(3)
    c1.metric("Age",      f"{age} yrs")
    c2.metric("BMI",      f"{bmi:.2f}")
    c3.metric("Smoker",   smoker)

    # BMI advice
    if bmi < 18.5:
        bmi_note = "⚠️ Underweight (BMI < 18.5)"
    elif bmi <= 24.9:
        bmi_note = "✅ Normal weight (18.5 – 24.9)"
    elif bmi <= 29.9:
        bmi_note = "⚠️ Overweight (25 – 29.9)"
    else:
        bmi_note = "🔴 Obese (BMI ≥ 30)"
    st.info(f"BMI category: {bmi_note}")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Model: Linear Regression | Dataset: insurance.csv | "
    "Encoding — Sex: male=0, female=1 | Smoker: yes=0, no=1 | "
    "Region: southeast=0, southwest=1, northeast=2, northwest=3"
)