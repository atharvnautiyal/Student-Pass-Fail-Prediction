# Student Performance Prediction

A small machine learning project that predicts whether a student is likely to **pass or fail** based on demographic and preparation features.

The project demonstrates a basic end-to-end ML workflow including data preprocessing, model training, evaluation, and a simple web interface using Streamlit.

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- MySQL
- Streamlit
- Joblib

---

## Project Structure

```
Student-Pass-Fail-Predictor
│
├── app
│   └── streamlit_app.py
│
├── model
│   ├── train_model.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── images
│   └── app_screenshot.png
│
├── requirements.txt
└── README.md
```

## Dataset

The dataset contains information about students including:

- Gender
- Race/Ethnicity
- Parental education level
- Lunch type
- Test preparation course
- Math, reading and writing scores

To convert this into a classification task:

Average Score = (math + reading + writing) / 3

Pass → Average ≥ 40
Fail → Average < 40

The model is then trained to predict **Pass/Fail** using the background features only.

---

## Model

Model used: **Logistic Regression**

Preprocessing steps:

- One-hot encoding for categorical variables
- Train/test split (80/20)
- Feature scaling using StandardScaler

Model accuracy:~77%

---

## Running the Project

Clone the repository
git clone https://github.com/YOUR_USERNAME/student-pass-fail-predictor.git

Install dependencies

pip install -r requirements.txt

Train the model

python model/train_model.py

Run the Streamlit app
streamlit run app/streamlit_app.py

---

## Application Preview

images/image.png

---

## Possible Improvements

- Try other models (Random Forest, XGBoost)
- Deploy the Streamlit app online
- Add more evaluation metrics
- Add dataset validation
