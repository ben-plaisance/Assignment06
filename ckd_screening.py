import json
from urllib.request import urlopen

import pandas as pd

BASE_URL = 'https://ruby.ils.unc.edu/~kibria/chip705_2026_fall/'


def calculate_egfr(age, sex, creatinine):
    """Calculate eGFR using the original Milestone 1 equation."""
    k, a, multiplier = (0.7, -0.241, 1.012) if sex == 'F' else (0.9, -0.302, 1)
    low = min(creatinine / k, 1)
    high = max(creatinine / k, 1)
    return 142 * low**a * high**-1.200 * 0.9938**age * multiplier


def calculate_bmi(height, weight):
    """Calculate BMI assuming height in inches and weight in pounds."""
    return 703 * weight / height**2


def load_patients():
    """Retrieve both datasets and return a DataFrame of screened patients."""
    demographics = pd.read_csv(BASE_URL + 'patient_demographics.csv', dtype={'patient_id': str})
    with urlopen(BASE_URL + 'cmp.json', timeout=30) as response:
        cmp_data = json.load(response)
    return screen_patients(demographics, cmp_data)


def screen_patients(demographics, cmp_data):
    """Match patients to creatinine results and retain eGFR <= 65."""
    results = []
    for patient in demographics.to_dict('records'):
        creatinine = next((float(test['patient_measure'])
                           for test in cmp_data.get(str(patient['patient_id']), [])
                           if test['measure'] == 'Creatinine'), None)
        if creatinine is None or creatinine <= 0:
            continue
        age = int(patient['age'])
        sex = patient['sex']
        height = float(patient['height'])
        weight = float(patient['weight'])
        egfr = calculate_egfr(age, sex, creatinine)
        if egfr <= 65:
            results.append([age, height, weight, calculate_bmi(height, weight), sex, egfr])
    return pd.DataFrame(results, columns=['age', 'height', 'weight', 'BMI', 'sex', 'eGFR'])
