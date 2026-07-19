import streamlit as st 
import requests

st.set_page_config(
    page_title="Student Health Risk Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded")
st.markdown(
    """
    <style>

    /* Main page padding */
    .main {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Center the title */
    h1 {
        text-align: center;
        color: #1E88E5;
    }

    /* Improve button appearance */
    div.stButton > button {
        width: 100%;
        height: 3.5em;
        border-radius: 12px;
        border: none;
        font-size: 18px;
        font-weight: bold;
    }

    /* Rounded input widgets */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title and all:-
st.title("🏥 Student Health Risk Predictor")

st.markdown("""
Predict a student's **health condition**
using lifestyle and fitness information.

Fill in the details below and click **Predict**.
""")

st.divider()

with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
        This application predicts
        student health condition
        using a trained CatBoost model.
        """)
    st.divider()
    st.metric("Model", "CatBoost")
    st.metric("Features", "13")
    st.metric("Classes", "3")
    st.caption("Made with using Streamlit & FastAPI")

# Layout:-
col1,col2 = st.columns(2)

# Col1 inpts:-
with col1:
    sleep_duration = st.slider(
        "Sleep Duration (Hours)",
        min_value = 0.0,
        max_value = 24.0,
        value = 7.0,
        step = 0.5
    )

    heart_rate = st.number_input(
        "heart Rate (BPM)",
        min_value=30.0,
        max_value=220.0,
        value = 72.0)

    bmi = st.number_input(
        "BMI",
        min_value = 10.0,
        max_value = 60.0,
        value = 22.5
    )    

    calorie_expenditure = st.number_input(
        "Calories Burned",
        min_value = 0.0,
        value = 600.0
    )

    water_intake = st.slider(
        "Water Intake (Liters)",
        min_value=0.0,
        max_value=10.0,
        value=2.5,
        step=0.1
    )

# Col2 Inputs:-
with col2:
    step_count = st.number_input(
        "Daily Step Counts",
        min_value = 0,
        value = 5000,
        step = 100
    )

    exercise_duration = st.slider(
        "Exercise Duration (Minutes)",
        min_value = 0,
        max_value = 300,
        value = 60 , 
        step =5
    )
    
    diet_type = st.selectbox(
        "Diet Type",
        options=["balanced","veg","non-veg"]
    )

    stress_level =st.selectbox(
        "Stress Level",
        options = ["low","medium","high"]
    )
    
    sleep_quality = st.selectbox(
        "Sleep Quality",
        options = ["good","poor"]
    )

    physical_activity_level = st.selectbox(
        "Physical Activity Level",
        options=["sedentary", "moderate", "active"]
    )

    smoking_alcohol = st.selectbox(
        "Smoking / Alcohol",
        options=["no", "occasional", "yes"]
    )

    gender = st.selectbox(
        "Gender",
        options=["male", "female", "other"]
    )

# Predict Button:
st.divider()

predict = st.button(
    "🔍 Predict Health Condition",
    use_container_width=True
)

if predict:

    data = {
        "sleep_duration": sleep_duration,
        "heart_rate": heart_rate,
        "bmi": bmi,
        "calorie_expenditure": calorie_expenditure,
        "step_count": step_count,
        "exercise_duration": exercise_duration,
        "water_intake": water_intake,
        "diet_type": diet_type,
        "stress_level": stress_level,
        "sleep_quality": sleep_quality,
        "physical_activity_level": physical_activity_level,
        "smoking_alcohol": smoking_alcohol,
        "gender": gender
    }

    try:
        with st.spinner("Predicting health condition..."):

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data
            )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"].lower()
            confidence = result["confidence"]

            st.subheader("Prediction Result")

            if prediction == "fit":
                st.success(f"✅ Health Condition: {prediction.title()}")

            elif prediction == "at-risk":
                st.warning(f"⚠️ Health Condition: {prediction.title()}")

            else:
                st.error(f"🚨 Health Condition: {prediction.title()}")

            st.metric(
                label="Prediction Confidence",
                value=f"{confidence:.2%}"
            )

        else:
            st.error(f"API Error ({response.status_code})")

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Could not connect to the FastAPI server.\n\n"
            "Make sure your FastAPI application is running."
        )

    except Exception as e:
        st.error(f"Unexpected Error: {e}")