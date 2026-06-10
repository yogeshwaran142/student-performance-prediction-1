# 🎓 Student Performance Prediction

An AI-based Machine Learning project that predicts whether a student will **Pass or Fail** based on key academic factors like study hours, attendance, previous scores, and assignment completion.

---

## 📌 Project Overview

This project applies **Logistic Regression** to classify student outcomes using a real-world-style dataset of 200 student records. It demonstrates end-to-end ML workflow — from data loading and preprocessing to model training, evaluation, and prediction.


---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data loading & manipulation |
| NumPy | Numerical operations |
| Scikit-learn | ML model (Logistic Regression) |

---

## 📂 Project Structure

```
student-performance-prediction/
│
├── dataset.csv              # 200-row student dataset
├── student_prediction.py    # Main ML script
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 📊 Dataset Features

| Column | Description |
|--------|-------------|
| `student_id` | Unique student identifier |
| `study_hours` | Daily average study hours (1–12) |
| `attendance_pct` | Attendance percentage (40–100%) |
| `previous_score` | Previous exam score (30–100) |
| `assignments_completed` | Assignments completed out of 10 |
| `result` | Target — 1 = Pass, 0 = Fail |

---

## ⚙️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/yogeshwaran142/student-performance-prediction-1.git
cd student-performance-prediction-1
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the prediction script**
```bash
python student_prediction.py
```

---

## 📈 Sample Output

```
Dataset Overview:
   student_id  study_hours  attendance_pct  previous_score  assignments_completed  result
0           1          5.1              63              87                      1       0
1           2         11.5              91              84                      4       1
...

Total Records: 200 | Pass: 124 | Fail: 76

Model Accuracy: 100.00%

Classification Report:
              precision    recall  f1-score   support
        Fail       1.00      1.00      1.00         9
        Pass       1.00      1.00      1.00        31

Sample Prediction:
  Study Hours: 7 | Attendance: 85% | Prev Score: 70 | Assignments: 8/10
  Result: Pass
```

---

## 🔍 Key Insights

- Students with **study hours > 7** and **attendance > 80%** have a significantly higher pass rate
- **Assignment completion** is a strong predictor of academic success
- The model achieves **high accuracy** on the test set using Logistic Regression

---

## 👨‍💻 Author

**Yogeshwaran J**  
B.Tech – Artificial Intelligence & Data Science (2026)  
