import math  # For sigmoid in ML
import requests  # Simulated for API calls (replace with real API in production)

# Simulated ML Model: Logistic Regression for Sepsis Risk
class SimpleLogisticRegression:
    def __init__(self):
        # Hypothetical weights (from "training" on 1000 samples, AUC ~0.82)
        self.weights = {'age': 0.02, 'temp': 0.5, 'hr': 0.3, 'wbc': 0.1, 'intercept': -2.0}
    
    def predict_proba(self, features):
        logit = self.weights['intercept']
        logit += self.weights['age'] * features['age']
        logit += self.weights['temp'] * (features['temp'] - 37)  # Centered at normal
        logit += self.weights['hr'] * (features['hr'] - 70)
        logit += self.weights['wbc'] * (features['wbc'] - 8000)
        prob = 1 / (1 + math.exp(-logit))  # Sigmoid
        return prob

# Simulated NLP Processor for Symptoms
class SimpleNLPProcessor:
    def extract_keywords(self, symptom_text):
        # Basic keyword extraction (in reality, use spaCy or BERT)
        keywords = []
        if 'fever' in symptom_text.lower(): keywords.append('fever')
        if 'shortness of breath' in symptom_text.lower(): keywords.append('shortness_of_breath')
        if 'cough' in symptom_text.lower(): keywords.append('cough')
        return keywords

# Simulated API for Drug Interactions
def check_drug_interactions(drugs, current_meds):
    # Mock API call (e.g., to Drugs.com API)
    interactions = []
    for drug in drugs:
        if drug in current_meds:
            interactions.append(f"Potential interaction: {drug} with {current_meds}")
    return interactions

# Patient Database Class with Historical Data
class PatientDatabase:
    def __init__(self):
        self.patients = {
            'Alice Johnson': {
                'age': 45,
                'historical_diagnoses': ['Pneumonia (2019, Amoxicillin, resolved)', 'UTI (2021, Ciprofloxacin, resolved)'],
                'treatments_outcomes': 'Good response to fluoroquinolones; no allergies.',
                'comorbidities': [],
                'allergies': [],
                'preferred_meds': ['Ciprofloxacin'],
                'avoid_meds': []
            },
            'Bob Smith': {
                'age': 62,
                'historical_diagnoses': ['Sepsis (2020, Piperacillin-tazobactam, resolved with renal side effects)', 'Cellulitis (2022, Clindamycin, partial response)'],
                'treatments_outcomes': 'Avoid beta-lactams due to renal issues; moderate Clindamycin response.',
                'comorbidities': ['Chronic kidney disease'],
                'allergies': [],
                'preferred_meds': ['Clindamycin'],
                'avoid_meds': ['Piperacillin-tazobactam']
            },
            'Carol Lee': {
                'age': 28,
                'historical_diagnoses': ['Bronchitis (2018, Azithromycin, resolved)', 'Sinusitis (2020, Amoxicillin, allergic reaction)'],
                'treatments_outcomes': 'Penicillin allergy; good macrolide response.',
                'comorbidities': ['Asthma'],
                'allergies': ['Penicillin'],
                'preferred_meds': ['Azithromycin'],
                'avoid_meds': ['Amoxicillin']
            },
            'David Kim': {
                'age': 55,
                'historical_diagnoses': ['Sepsis (2019, Vancomycin, resolved)', 'MRSA (2021, Linezolid, resolved)'],
                'treatments_outcomes': 'Resistant to methicillin; effective with vancomycin analogs.',
                'comorbidities': ['Diabetes'],
                'allergies': [],
                'preferred_meds': ['Linezolid'],
                'avoid_meds': ['Methicillin']
            },
            'Emma Patel': {
                'age': 70,
                'historical_diagnoses': ['UTI (2020, Nitrofurantoin, resolved)', 'Pneumonia (2022, Levofloxacin, resolved)'],
                'treatments_outcomes': 'Good quinolone response; dose adjustments for age.',
                'comorbidities': ['Hypertension'],
                'allergies': [],
                'preferred_meds': ['Levofloxacin'],
                'avoid_meds': []
            },
            'Frank Garcia': {
                'age': 35,
                'historical_diagnoses': ['Skin abscess (2019, Trimethoprim-sulfamethoxazole, resolved)', 'Gastroenteritis (2021, Ciprofloxacin, resolved)'],
                'treatments_outcomes': 'Effective with TMP-SMX; no issues.',
                'comorbidities': [],
                'allergies': [],
                'preferred_meds': ['Trimethoprim-sulfamethoxazole'],
                'avoid_meds': []
            },
            'Gina Rossi': {
                'age': 50,
                'historical_diagnoses': ['Sepsis (2020, Meropenem, resolved)', 'Fungal infection (2022, Fluconazole, resolved)'],
                'treatments_outcomes': 'Carbapenem effective; fungal history.',
                'comorbidities': ['Immunodeficiency'],
                'allergies': [],
                'preferred_meds': ['Meropenem', 'Fluconazole'],
                'avoid_meds': []
            },
            'Henry Wong': {
                'age': 40,
                'historical_diagnoses': ['Bronchitis (2018, Doxycycline, resolved)', 'Lyme (2020, Amoxicillin, resolved)'],
                'treatments_outcomes': 'Tetracycline effective; no penicillin issues.',
                'comorbidities': [],
                'allergies': [],
                'preferred_meds': ['Doxycycline'],
                'avoid_meds': []
            },
            'Iris Thompson': {
                'age': 65,
                'historical_diagnoses': ['Pneumonia (2019, Ceftriaxone, resolved)', 'Sepsis (2021, Piperacillin-tazobactam partial, switched to Imipenem)'],
                'treatments_outcomes': 'Initial beta-lactam resistance; Imipenem successful.',
                'comorbidities': ['COPD'],
                'allergies': [],
                'preferred_meds': ['Imipenem'],
                'avoid_meds': ['Piperacillin-tazobactam']
            },
            'Jack Nguyen': {
                'age': 30,
                'historical_diagnoses': ['Sinusitis (2019, Amoxicillin, resolved)', 'Ear infection (2021, Azithromycin, resolved)'],
                'treatments_outcomes': 'Good response to both; interchangeable.',
                'comorbidities': [],
                'allergies': [],
                'preferred_meds': ['Amoxicillin', 'Azithromycin'],
                'avoid_meds': []
            }
        }
    
    def get_patient(self, name):
        return self.patients.get(name, None)

# Function to Query Patient by Name
def query_patient(database):
    name = input("Enter patient's name: ").strip()
    patient_history = database.get_patient(name)
    if not patient_history:
        print(f"No historical data found for {name}. Proceeding with general CDSS.")
        return None
    print(f"\nHistorical Details for {name}:")
    print(f"- Age: {patient_history['age']}")
    print(f"- Diagnoses: {', '.join(patient_history['historical_diagnoses'])}")
    print(f"- Treatments/Outcomes: {patient_history['treatments_outcomes']}")
    print(f"- Comorbidities: {', '.join(patient_history['comorbidities']) if patient_history['comorbidities'] else 'None'}")
    print(f"- Allergies: {', '.join(patient_history['allergies']) if patient_history['allergies'] else 'None'}")
    return patient_history

# Main CDSS Function with Historical Integration
def cdss_antibiotic_suggestion(patient_data, ml_model=None, nlp_processor=None, patient_history=None):
    # Input validation
    required_keys = ['temperature', 'heart_rate', 'white_blood_cell_count', 'symptoms', 'current_medications']
    if not all(key in patient_data for key in required_keys):
        return {"error": "Missing required patient data fields."}
    
    temp = patient_data['temperature']
    hr = patient_data['heart_rate']
    wbc = patient_data['white_blood_cell_count']
    symptoms = patient_data['symptoms']
    current_meds = patient_data['current_medications']
    
    # Incorporate History
    if patient_history:
        allergies = patient_history['allergies']
        avoid_meds = patient_history['avoid_meds']
        preferred_meds = patient_history['preferred_meds']
        comorbidities = patient_history['comorbidities']
        age = patient_history['age']
    else:
        allergies = patient_data.get('allergies', [])
        avoid_meds = []
        preferred_meds = []
        comorbidities = patient_data.get('comorbidities', [])
        age = patient_data.get('age', 50)  # Default
    
    # NLP Processing
    if nlp_processor:
        extracted_symptoms = nlp_processor.extract_keywords(symptoms)
    else:
        extracted_symptoms = symptoms if isinstance(symptoms, list) else [symptoms]
    
    # Rule-Based Check: qSOFA Score
    qsofa_score = 0
    if temp > 38 or temp < 36: qsofa_score += 1
    if hr > 100: qsofa_score += 1
    if wbc < 4000 or wbc > 12000: qsofa_score += 1
    
    # ML Prediction
    sepsis_prob = 0.0
    if ml_model:
        features = {'age': age, 'temp': temp, 'hr': hr, 'wbc': wbc}
        sepsis_prob = ml_model.predict_proba(features)
    
    # Decision Logic with History
    suggested_drugs = []
    if sepsis_prob > 0.7 or qsofa_score >= 2:
        alert = f"High sepsis risk (qSOFA: {qsofa_score}, ML Prob: {sepsis_prob:.2f}). Urgent evaluation needed."
        if 'penicillin' not in allergies and 'Piperacillin-tazobactam' not in avoid_meds:
            if 'Piperacillin-tazobactam' in preferred_meds:
                suggested_drugs = ['Piperacillin-tazobactam']
            else:
                suggested_drugs = ['Piperacillin-tazobactam']
        elif preferred_meds:
            suggested_drugs = preferred_meds[:2]
        else:
            suggested_drugs = ['Ciprofloxacin', 'Metronidazole']
        if 'shortness_of_breath' in extracted_symptoms:
            alert += " Hypoxemia likely; consider ventilatory support."
    elif sepsis_prob > 0.3 or qsofa_score == 1:
        alert = f"Moderate risk (qSOFA: {qsofa_score}, ML Prob: {sepsis_prob:.2f}). Monitor closely."
        suggested_drugs = ['Procalcitonin test'] if not preferred_meds else preferred_meds[:1]
    else:
        alert = f"Low risk (qSOFA: {qsofa_score}, ML Prob: {sepsis_prob:.2f})."
        suggested_drugs = []
    
    # Check for avoided meds
    for med in suggested_drugs[:]:  # Copy to avoid modification during iteration
        if med in avoid_meds:
            alert += f" Historical contraindication: Avoid {med} based on past issues."
            suggested_drugs.remove(med)
    
    # API Check for Interactions
    interactions = check_drug_interactions(suggested_drugs, current_meds)
    if interactions:
        alert += f" Drug interactions detected: {', '.join(interactions)}. Consult pharmacist."
    
    # Additional Recommendations
    suggestion = f"Suggested actions: {', '.join(suggested_drugs) if suggested_drugs else 'None'}."
    if age > 65:
        suggestion += " Adjust dosing for renal function (e.g., eGFR)."
    if 'diabetes' in comorbidities:
        suggestion += " Monitor glucose closely during therapy."
    if 'cough' in extracted_symptoms:
        suggestion += " Consider chest X-ray for pneumonia."
    
    return {
        "alert": alert,
        "suggestion": suggestion,
        "evidence": "Based on IDSA guidelines (2021), qSOFA (JAMA, 2016), simulated ML (AUC 0.82), and patient history.",
        "extracted_symptoms": extracted_symptoms,
        "interactions": interactions,
        "historical_insight": f"Preferred meds: {', '.join(preferred_meds) if preferred_meds else 'None'}; Avoid: {', '.join(avoid_meds) if avoid_meds else 'None'}"
    }

# Example Usage
database = PatientDatabase()
ml_model = SimpleLogisticRegression()
nlp_processor = SimpleNLPProcessor()

# Simulate query (in real use, this would be interactive)
patient_history = query_patient(database)  # User inputs, e.g., "Bob Smith"

if patient_history:
    # Merge with current data
    current_data = {
        'temperature': 39.0,
        'heart_rate': 105,
        'white_blood_cell_count': 14000,
        'symptoms': 'Patient reports fever, shortness of breath.',
        'current_medications': ['Aspirin']
    }
    patient_data = {**current_data, **patient_history}
else:
    patient_data = {
        'age': 50,
        'temperature': 39.0,
        'heart_rate': 105,
        'white_blood_cell_count': 14000,
        'allergies': [],
        'symptoms': 'Patient reports fever, shortness of breath.',
        'current_medications': ['Aspirin'],
        'comorbidities': []
    }

output = cdss_antibiotic_suggestion(patient_data, ml_model, nlp_processor, patient_history)
print("\nCDSS Output:")
for key, value in output.items():
    print(f"{key}: {value}")

