import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = {
    'study_hours': [2, 4, 6, 8, 10],
    'attendance': [60, 70, 80, 90, 95],
    'result': [0, 0, 1, 1, 1]
}


df = pd.DataFrame(data)
print(df)
X = df[['study_hours', 'attendance']]
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)
prediction = model.predict([[7, 85]])
print("Prediction (1 = Pass, 0 = Fail):", prediction[0])
