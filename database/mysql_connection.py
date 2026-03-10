import pandas as pd
import mysql.connector

#load data from csv file
df = pd.read_csv(r"C:\Users\Atharv\Desktop\Atharv\VS CODE\Projects\Student_Pass_Fail_Prediction\data\StudentsPerformance.csv")

#connect mysql
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123@123",
    database = "student_ml_project"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO student_performace (
        gender,
        race_ethnicity,
        parental_education,
        lunch,
        test_prep,
        math_score,
        reading_score,
        writing_score
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
        row["gender"],
        row["race/ethnicity"],
        row["parental level of education"],
        row["lunch"],
        row["test preparation course"],
        row["math score"],
        row["reading score"],
        row["writing score"]
    ))

conn.commit()
conn.close()