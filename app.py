
import streamlit as st
import pandas as pd
import joblib

# Configure the website
st.set_page_config(
    page_title="SereneHeart AI",
    page_icon="❤️",
    layout="wide"
)

# Load the trained machine learning model
model = joblib.load("heart_disease_model.joblib")

# Website heading
st.title("SereneHeart AI")

st.subheader("Heart Disease Classification Using Machine Learning")

st.write(
    "Welcome to SereneHeart AI! This application uses a trained "
    "machine learning model to classify heart disease presence "
    "based on patient health information."
)

st.info(
    "Educational project only. This application is not a medical "
    "diagnosis tool and should not replace professional medical advice."
)

st.success("Machine learning model loaded successfully!")

# Patient information form
st.divider()
st.header("Patient Health Information")
st.write("Enter the patient's information below.")

with st.form("patient_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age (years)", 1, 120, 50)
        sex = st.selectbox(
            "Sex", ["Female", "Male"]
        )
        cp = st.selectbox(
            "Chest Pain Type",
            [
                "Typical angina",
                "Atypical angina",
                "Non-anginal pain",
                "Asymptomatic"
            ]
        )
        trestbps = st.number_input(
            "Resting Blood Pressure (mm Hg)", 50, 250, 120
        )
        chol = st.number_input(
            "Serum Cholesterol (mg/dL)", 50, 700, 200
        )
        fbs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dL",
            ["No", "Yes"]
        )
        restecg = st.selectbox(
            "Resting ECG Result",
            ["Normal", "ST-T abnormality", "Left ventricular hypertrophy"]
        )

    with col2:
        thalach = st.number_input(
            "Maximum Heart Rate Achieved", 40, 250, 150
        )
        exang = st.selectbox(
            "Exercise-Induced Angina", ["No", "Yes"]
        )
        oldpeak = st.number_input(
            "ST Depression (Oldpeak)", 0.0, 10.0, 1.0, 0.1
        )
        slope = st.selectbox(
            "Slope of Peak Exercise ST Segment",
            ["Upsloping", "Flat", "Downsloping"]
        )
        ca = st.selectbox(
            "Number of Major Vessels (0–3)", [0, 1, 2, 3]
        )
        thal = st.selectbox(
            "Thalassemia",
            ["Normal", "Fixed defect", "Reversible defect"]
        )

    submitted = st.form_submit_button(
        "Predict Heart Disease Classification",
        use_container_width=True
    )

if submitted:
    patient = pd.DataFrame([{
        "age": age,
        "sex": 0 if sex == "Female" else 1,
        "cp": [
            "Typical angina",
            "Atypical angina",
            "Non-anginal pain",
            "Asymptomatic"
        ].index(cp) + 1,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": 0 if fbs == "No" else 1,
        "restecg": [
            "Normal",
            "ST-T abnormality",
            "Left ventricular hypertrophy"
        ].index(restecg),
        "thalach": thalach,
        "exang": 0 if exang == "No" else 1,
        "oldpeak": oldpeak,
        "slope": [
            "Upsloping", "Flat", "Downsloping"
        ].index(slope) + 1,
        "ca": ca,
        "thal": {
            "Normal": 3,
            "Fixed defect": 6,
            "Reversible defect": 7
        }[thal]
    }])
# Website design and colors
st.markdown("""
<style>
    .stApp {
        background-color: #F0F8F8;
        color: #102B46;
    }

    h1, h2, h3 {
        color: #102B46 !important;
        font-family: Arial, sans-serif;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        background-color: #157C83;
        color: white;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 12px 20px;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background-color: #102B46;
        color: white;
    }

    [data-testid="stForm"] {
        background-color: white;
        border-radius: 18px;
        padding: 20px;
        border: 1px solid #D8E8E8;
    }
</style>
""", unsafe_allow_html=True)

    prediction = model.predict(patient)[0]

    st.subheader("Classification Result")

    if prediction == 1:
        st.warning(
            "The model classifies this record as showing "
            "heart disease presence in the training dataset."
        )
    else:
        st.success(
            "The model classifies this record as showing "
            "no heart disease presence in the training dataset."
        )

    st.caption(
        "This prediction is for educational purposes only. "
        "It cannot diagnose heart disease or predict future "
        "heart disease."
    )

