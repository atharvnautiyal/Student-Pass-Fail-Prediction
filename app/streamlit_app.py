import streamlit as st
import pandas as pd
import joblib

st.subheader("Model Information")
st.write("Model Used: Logistic Regression")
# Load model and preprocessing files
model = joblib.load("model\model.pkl")
scaler = joblib.load("model\scaler.pkl")
feature_columns = joblib.load(r"model\feature_columns.pkl")
accuracy = joblib.load("model\model_accuracy.pkl")
st.write("Model Accuracy:", round(accuracy*100,2), "%")

st.title("🎓 Student Performance Predictor")

st.write("""
This app predicts whether a student is likely to **PASS or FAIL**
based on demographic and preparation factors.
""")

# User Inputs
gender = st.selectbox("Gender", ["male", "female"])

race = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

education = st.selectbox(
    "Parental Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])

prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

st.divider()

if st.button("Predict Result"):

    input_data = {
        "gender": gender,
        "race_ethnicity": race,
        "parental_education": education,
        "lunch": lunch,
        "test_prep": prep
    }

    input_df = pd.DataFrame([input_data])

    # Apply same encoding as training
    input_df = pd.get_dummies(input_df)

    # Align columns with training features
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Student Likely to PASS")
    else:
        st.error("⚠️ Student Likely to FAIL")

    st.write("Confidence:", round(probability[0][1]*100, 2), "%")