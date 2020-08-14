from flask import Flask, render_template, request
import requests
import jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("houseprice.pkl", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
     if request.method == 'POST':
         Area = float(request.form['Area'])
         BHK = int(request.form['BHK'])
         Bathroom = float(request.form['Bathroom'])
         Parking = float(request.form['Parking'])
         Furnishing = (request.form['Furnishing'])
         if (Furnishing=='Semi Furnished'):
             Furnishing_semi = 1
             Furnishing_Unfur = 0
         elif (Furnishing == 'Un Furnished'):
            Furnishing_semi = 0
            Furnishing_Unfur = 1
         else:
            Furnishing_semi = 0
            Furnishing_Unfur = 0

         Transaction = int(request.form['Transaction'])
         Type = int(request.form['Type'])



         prediction=model.predict([Area,BHK,Bathroom,Parking,Furnishing_semi,Furnishing_Unfur,Transaction,Type])[0]


         return render_template('index.html',prediction_texts=prediction)



if __name__=="__main__":
    app.run(debug=True)
