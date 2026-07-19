# 🏥 Student Health Risk Prediction

An end-to-end Machine Learning project that predicts a student's health condition using lifestyle, physical activity, dietary habits, and physiological measurements.

The project demonstrates the complete ML workflow—from data preprocessing and model development to deployment through a FastAPI backend and an interactive Streamlit application.

---

## 📌 Project Overview

This application predicts whether a student is:

- ✅ Fit
- ⚠️ At-Risk
- ❌ Unhealthy

based on various health and lifestyle indicators.

The goal is to assist in the early identification of potential health risks using machine learning.

---

## 🚀 Features

- End-to-end Machine Learning pipeline
- Automated data preprocessing using Scikit-learn Pipeline
- CatBoost classifier for prediction
- FastAPI REST API
- Interactive Streamlit web application
- Confidence score for each prediction
- Robust handling of missing values and unseen categories

---

## 📊 Dataset

**Source:** Kaggle Playground Series – Student Health Risk Prediction

### Input Features

### Numerical
- Sleep Duration
- Heart Rate
- BMI
- Calorie Expenditure
- Step Count
- Exercise Duration
- Water Intake

### Categorical
- Diet Type
- Stress Level
- Sleep Quality
- Physical Activity Level
- Smoking & Alcohol
- Gender

### Target

- Health Condition

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

- Median Imputation for numerical features
- Missing value handling for categorical features
- Standard Scaling
- One-Hot Encoding
- ColumnTransformer
- Integrated Scikit-learn Pipeline

---

## 🤖 Model Selection

Multiple machine learning models were evaluated before selecting the final model.

Models explored:

- Logistic Regression
- Random Forest
- XGBoost
- **CatBoost (Final Model)**

CatBoost achieved the best overall performance and was selected for deployment.

---

## 📈 Results

**Final Model:** CatBoost Classifier

### Performance

- Accuracy: **~97%**
- Strong performance across all three classes
- Good generalization on unseen validation data

---

## 🔍 Key Findings

- Sleep duration is one of the strongest predictors of student health.
- High stress levels are strongly associated with the **At-Risk** and **Unhealthy** classes.
- BMI and heart rate contribute significantly to prediction accuracy.
- Physical activity and exercise duration improve prediction performance.
- Removing demographic features such as gender had little impact on overall accuracy but slightly reduced recall for minority classes.

---

## 🖥️ Application

### FastAPI Backend

- Receives user input
- Performs preprocessing
- Generates predictions
- Returns prediction confidence

### Streamlit Frontend

Users can:

- Enter health information
- Predict health condition instantly
- View prediction confidence through a simple interface

---

## 📁 Project Structure

```
student-health-risk-prediction/
│
├── api/
│   └── app.py
│
├── model/
│   └── catboost_pipeline.pkl
│
├── streamlit_app/
│   └── app.py
│
├── data/
├── notebooks/
├── README.md
└── .gitignore
```

---

## 📸 Screenshots

### <img width="2796" height="1580" alt="image" src="https://github.com/user-attachments/assets/bc190d11-3a29-4219-b5c3-ac3fb67cdd32" />


### Prediction Result
<img width="2748" height="862" alt="image" src="https://github.com/user-attachments/assets/47c70f04-0184-4c76-90da-6f18e680370f" />

---

## 🔮 Future Improvements

- Hyperparameter optimization
- Docker support
- Model monitoring

---

## 👨‍💻 Author

**Hitesh Sirswa**

GitHub: : https://github.com/hitesh-2212/


LinkedIn: : https://www.linkedin.com/in/hitesh-sirswa/
---

## ⭐ If you found this project useful, consider giving it a Star!
