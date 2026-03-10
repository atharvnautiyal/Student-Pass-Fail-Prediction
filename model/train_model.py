#importing libraries
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

#loading data
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@123",
    database="student_ml_project"
)

query = "SELECT * FROM student_performace"

df = pd.read_sql(query, conn)

conn.close()

#feature engineering 
df['avg_score'] = ((df['math_score'] + df['writing_score'] + df['reading_score']) / 3).round()
df['result'] = (df['avg_score'] >= 40).astype(int)

# Drop unnecessary columns
df = df.drop(columns=["id", "math_score", "reading_score", "writing_score", "avg_score"])

#encoding
df = pd.get_dummies(df, columns=[
    "gender",
    "race_ethnicity",
    "parental_education",
    "lunch",
    "test_prep"
], drop_first=True)

#features
X = df.drop("result", axis = 1)
y = df["result"]

#spilit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#model training
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)

# model evaluation
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(accuracy, 2))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

#confusion matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues",
            xticklabels=["Fail","Pass"],
            yticklabels=["Fail","Pass"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

#save model
joblib.dump(model, "model/model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(X.columns.tolist(), "model/feature_columns.pkl")
joblib.dump(accuracy, "model/model_accuracy.pkl")