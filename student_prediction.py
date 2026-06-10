import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv('dataset.csv', sep=None, engine='python')

print("Dataset Overview:")
print(df.head())
print(f"\nTotal Records: {len(df)} | Pass: {df['result'].sum()} | Fail: {(df['result']==0).sum()}")

# Features and target
X = df[['study_hours', 'attendance_pct', 'previous_score', 'assignments_completed']]
y = df['result']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))

# Sample Prediction
sample = pd.DataFrame([[7, 85, 70, 8]], 
    columns=['study_hours', 'attendance_pct', 'previous_score', 'assignments_completed'])
prediction = model.predict(sample)
print(f"\nSample Prediction:")
print(f"  Study Hours: 7 | Attendance: 85% | Prev Score: 70 | Assignments: 8/10")
print(f"  Result: {'Pass' if prediction[0] == 1 else 'Fail'}")
