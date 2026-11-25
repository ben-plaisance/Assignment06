# Descriptive Statistics: Kidney Disease Screening

This project extends Milestone 1 by retrieving synthetic patient demographics and CMP results from the UNC course website, matching records by patient ID, calculating eGFR and BMI, and examining patients with eGFR <= 65.

## Analysis plan
- Calculate descriptive statistics for age, height and weight.
- Compare average eGFR across adult BMI categories (underweight, healthy weight, overweight and obesity).
- Plot age against eGFR and visualize the distribution of patient sex.

The data are randomly generated and findings are not clinical conclusions. The code assumes demographic columns `height` (inches) and `weight` (pounds); verify these names and units against the source before interpreting BMI. Live source access was unavailable during preparation.

## Setup

```sh
python -m venv .venv
```

Activate on Windows PowerShell: `.venv\Scripts\Activate.ps1` (or on macOS/Linux: `source .venv/bin/activate`). Then run:

```sh
python -m pip install -r requirements.txt
python -m jupyter notebook
```

Open `main.ipynb`, select the virtual environment kernel, and run all cells. Internet access is required. `ckd_screening.py` contains the reusable data retrieval and calculation functions.
