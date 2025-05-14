from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)

model = joblib.load("model/logistic_regression_model.pkl")

FEATURES = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    message_type = None

    if request.method == "POST":
        if "file" in request.files and request.files["file"].filename != '':
            file = request.files["file"]
            try:
                df = pd.read_csv(file)
                if not all(f in df.columns for f in FEATURES):
                    raise ValueError(f"Uploaded file must contain columns: {FEATURES}")
                preds = model.predict(df[FEATURES])
                prediction = preds[0]
            except Exception as e:
                message = str(e)
                message_type = "warning"
        else:
            try:
                inputs = [float(request.form.get(f)) for f in FEATURES]
                input_array = np.array([inputs])
                prediction = model.predict(input_array)[0]
            except Exception as e:
                message = f"Invalid input: {e}"
                message_type = "warning"
            else:
                pass
        if message_type is None and message is None:
            if prediction == 1:
                message = "benign"
                message_type = "benign"
            else:
                message = "malignant"
                message_type = "malignant"

    return render_template("index.html", message=message, message_type=message_type, features=FEATURES)

if __name__ == "__main__":
    app.run(debug=True)
