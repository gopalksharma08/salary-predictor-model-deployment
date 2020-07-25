from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open("random_forest_mode.pkl", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Hours_per_week=float(request.form['Hours'])
        education_Doctorate=request.form['education_Doctorate']
        if (education_Doctorate == 'Doctorate'):
            education_Doctorate = 1
            education_High_school = 0
            education_Masters = 0
        elif (education_Doctorate =='High School'):
            education_Doctorate = 0
            education_High_school = 1
            education_Masters = 0
        elif (education_Doctorate =='Masters'):
            education_Doctorate = 0
            education_High_school = 0
            education_Masters = 1
        else:
            education_Doctorate = 0
            education_High_school = 0
            education_Masters = 0
        marital_status_Not_married=int(request.form['marital_status_Not_married'])
        sex_Male=int(request.form['sex_Male'])

        native_country_non_us=request.form['native_country_non_us']
        if(native_country_non_us=='US'):
            native_country_non_us= 1
        else:
            native_country_non_us= 0
        prediction=model.predict([[Age,Hours_per_week,education_Doctorate,education_High_school,education_Masters,marital_status_Not_married,sex_Male,native_country_non_us]])

        if prediction[0]== 0:
            return render_template('less.html')
        else:
            return render_template('greater.html')
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
