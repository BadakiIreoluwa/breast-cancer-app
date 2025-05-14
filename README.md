# Breast Cancer Prediction Application

This simple web application built with Flask utilizes Scikit-Learn's Logistic Regression Module to create a prediction of the nature of a tumour based on the UCI ML Breast Cancer Wisconsin (Diagnostic) dataset.

You can check out the site at [website_name.com]

This dataset is a binary classification dataset that classifies data with 0s representing malignant tumours and 1s representing benign tumours. The training process is outlined in the 'Tasks_and_models.ipynb' Notebook attached in the project. While the model is of relatively high accuracy, 98% based on the testing data, it would be ill advised to use this model in practical situations to determine the nature of a tumour due to the relative lack of rigour utilised in the training dataset.

---

## 📁 Project Structure

```text
breast_cancer_app/
├── app.py                              # Flask backend
├── requirements.txt                    # Python dependencies
├── templates/
│   └── index.html                      # HTML template for the UI
├── static/
│   └── css/
│       └── styles.css                  # External CSS file for styling
├── model/
│   └── logistic_regression_model.pkl   # Exported Logistic Regression Model
│   └── scaler.pkl                      # Exported Scaler
└── Tasks_and_models.ipynb              # Python Notebook file detailing methodology in training model 
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/BadakiIreoluwa/specimen-webapp.git
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App Locally

```bash
python app.py
```

Then open your browser and go to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

This project was completed as part of the completion of Covenant University's Bachelor of Computer Science degree for the course CSC 442 - Computational Biology II
