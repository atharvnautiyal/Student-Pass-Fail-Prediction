🎓 Student Performance Prediction System

A machine learning web application that predicts whether a student is likely to pass or fail based on demographic and preparation features.

This project demonstrates a complete machine learning pipeline including data storage, preprocessing, model training, evaluation, and deployment through an interactive web interface.

📌 Project Overview

Educational institutions often need to identify students who may be at risk of failing so that early interventions can be applied.

This project uses machine learning to predict student performance based on factors such as:

Gender
Race/Ethnicity
Parental education level
Lunch type
Test preparation course

The trained model is deployed through a Streamlit web application that allows users to input student information and receive a prediction in real time.

⚙️ Machine Learning Workflow
MySQL Database
      ↓
Data Extraction (Pandas)
      ↓
Feature Engineering
      ↓
Categorical Encoding (One-Hot Encoding)
      ↓
Train/Test Split
      ↓
Feature Scaling (StandardScaler)
      ↓
Logistic Regression Model
      ↓
Model Evaluation (Accuracy + Confusion Matrix)
      ↓
Model Saved with Joblib
      ↓
Streamlit Web Application for Predictions

🛠️ Tech Stack

=> Python

=> Pandas – Data manipulation

=> Scikit-learn – Machine learning

=> MySQL – Data storage

=> Streamlit – Web application interface

=> Matplotlib / Seaborn – Visualization

=> Joblib – Model persistence

📂 Project Structure
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
├── data
│   └── StudentsPerformance.csv
│
├── database
│   └── mysql_connection.py
│
├── images
│   └── app_screenshot.png
│
├── requirements.txt
├── README.md
└── .gitignore

🧠 Feature Engineering

The dataset contains individual subject scores.
To create a binary classification problem:

The average score of Math, Reading, and Writing is calculated.

Students are classified as:

Pass  → Average Score ≥ 40
Fail  → Average Score < 40

Unnecessary columns such as raw exam scores are removed so the model predicts performance based on background factors only.

🤖 Machine Learning Model

The model used is Logistic Regression, which is well suited for binary classification problems.
Key preprocessing steps include:
One-Hot Encoding for categorical features
Train-Test split (80/20)
Feature scaling using StandardScaler
Handling class imbalance using class_weight='balanced'

📊 Model Evaluation

The model is evaluated using:
Accuracy Score
Classification Report
Confusion Matrix

Example metrics:
Accuracy: ~78%

Confusion Matrix Visualization:
Actual vs Predicted

This helps analyze how well the model predicts both pass and fail cases.

🖥️ Streamlit Web Application

The trained model is integrated into a Streamlit web app that allows users to input student data and receive predictions instantly.

User Inputs:

Gender
Race/Ethnicity
Parental Education
Lunch Type
Test Preparation Course

Output:

Prediction: PASS / FAIL
Confidence Score
🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/student-pass-fail-predictor.git
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Train the model
python model/train_model.py

This will generate:

model.pkl
scaler.pkl
feature_columns.pkl
4️⃣ Run the Streamlit app
streamlit run app/streamlit_app.py

Then open the browser at:

http://localhost:8501

📷 Application Preview

images/image.png

Example:
Student Performance Predictor UI

🔮 Future Improvements

Possible enhancements for this project:
Try advanced models like Random Forest or XGBoost
Deploy the app online using Streamlit Cloud
Add model performance dashboard
Implement automated retraining pipeline
Add dataset validation and monitoring

🎯 Key Learnings

This project helped demonstrate:
End-to-end machine learning workflow
Feature engineering and preprocessing
Integration of ML with databases
Model deployment using Streamlit
Building a user-facing ML application

👨‍💻 Author

Atharv Nautiyal
Aspiring Machine Learning Engineer / Data Scientist

⭐ If you found this project useful
Feel free to star the repository ⭐ and share feedback.