from flask import Flask, render_template, redirect, url_for, request
import joblib
import numpy as np

app = Flask(__name__, template_folder= 'templates')

model = joblib.load('new_model.joblib')

scaler = joblib.load('new_scaler.joblib')

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    Pregnancies = float(request.form['Pregnancies'])
    Glucose = float(request.form['Glucose'])
    BloodPressure = float(request.form['BloodPressure'])
    SkinThickness = float(request.form['SkinThickness'])
    Insulin = float(request.form['Insulin'])
    BMI = float(request.form['BMI'])
    DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
    Age = float(request.form['Age'])

    cols = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    col_scaled = scaler.transform(cols)

    pred = model.predict(col_scaled)
    
    if pred[0] == 0:
        result = "NOT DIABETIC"
    else:
        result = "DIABETIC"
    
     
    return render_template('result.html', result=result)



if __name__ == '__main__':
    app.run(debug= True)