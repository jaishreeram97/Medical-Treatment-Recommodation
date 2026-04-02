from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.linear_model import LogisticRegression
import logging

# -------------------------------
# Logging Setup
# -------------------------------
logging.basicConfig(filename="audit.log", level=logging.INFO)

app = FastAPI(title="Hospital Innovation Lab CDSS")

# -------------------------------
# Dummy Model Training
# -------------------------------
# Generic training data for demonstration
X_train = np.array([
    [50, 1, 150, 7.0, 240],
    [30, 0, 120, 5.5, 180],
    [65, 1, 170, 8.0, 260],
    [40, 0, 130, 6.0, 200]
])
y_train = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X_train, y_train)

# -------------------------------
# Patient Schema
# -------------------------------
class Patient(BaseModel):
    age: int
    gender: int  # 0 = female, 1 = male
    systolic_bp: float
    hba1c: float
    cholesterol: float
    bmi: float = 25
    smoker: int = 0
    lactate: float = 1.0
    sofa_score: float = 2.0
    wbc: float = 7000
    cancer_stage: int = 1

# -------------------------------
# Rule Engine
# -------------------------------
def rule_engine(domain, patient):
    alerts = []

    if domain == "cardiology":
        if patient.systolic_bp > 160:
            alerts.append("Severe hypertension alert")
        if patient.smoker:
            alerts.append("Smoking risk factor")

    elif domain == "emergency":
        if patient.lactate > 2:
            alerts.append("Possible sepsis risk")

    elif domain == "icu":
        if patient.sofa_score >= 6:
            alerts.append("High ICU mortality risk")

    elif domain == "endocrinology":
        if patient.hba1c >= 7:
            alerts.append("Poor glycemic control")

    elif domain == "oncology":
        if patient.wbc < 4000:
            alerts.append("Neutropenia risk")

    return alerts

# -------------------------------
# Recommendation Engine
# -------------------------------
def generate_recommendation(domain, patient):
    features = np.array([[
        patient.age,
        patient.gender,
        patient.systolic_bp,
        patient.hba1c,
        patient.cholesterol
    ]])

    risk_prob = model.predict_proba(features)[0][1]
    alerts = rule_engine(domain, patient)
    recommendations = []

    if domain == "cardiology":
        if risk_prob > 0.7:
            recommendations.append("Refer to cardiology specialist.")
        if patient.bmi >= 30:
            recommendations.append("Start weight management plan.")

    elif domain == "emergency":
        if risk_prob > 0.6:
            recommendations.append("Prioritize triage level.")
        if patient.lactate > 2:
            recommendations.append("Initiate sepsis protocol.")

    elif domain == "icu":
        if risk_prob > 0.75:
            recommendations.append("Escalate ICU monitoring.")

    elif domain == "endocrinology":
        if patient.hba1c > 8:
            recommendations.append("Adjust insulin regimen.")

    elif domain == "oncology":
        if patient.cancer_stage >= 3:
            recommendations.append("Review chemotherapy plan.")

    result = {
        "domain": domain,
        "risk_probability": float(risk_prob),
        "alerts": alerts,
        "recommendations": recommendations
    }

    logging.info(f"{domain} evaluation: {result}")

    return result

# -------------------------------
# API Endpoints
# -------------------------------
@app.post("/evaluate/{domain}")
def evaluate(domain: str, patient: Patient):
    domain = domain.lower()

    if domain not in ["cardiology", "emergency", "icu", "endocrinology", "oncology"]:
        return {"error": "Invalid domain"}

    return generate_recommendation(domain, patient)

@app.get("/")
def root():
    return {"message": "Hospital Innovation Lab CDSS Running"}
