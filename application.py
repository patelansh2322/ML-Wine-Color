from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## import grid and standard scaler pickle files
grid_model = pickle.load(open('models/grid.pkl', 'rb'))
scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=="POST":
        Citric_Acid = float(request.form.get('citric acid'))
        Residual_Sugar = float(request.form.get('residual sugar'))
        Free_Sulphur_Dioxide = float(request.form.get('free sulphur dioxide'))
        Total_Sulphur_Dioxide = float(request.form.get('total sulphur dioxide'))
        pH = float(request.form.get('pH'))
        Alcohol = float(request.form.get('alcohol'))
        Quality = float(request.form.get('quality'))

        new_data_scaled = scaler_model.transform([[Citric_Acid, Residual_Sugar, Free_Sulphur_Dioxide, Total_Sulphur_Dioxide, pH, Alcohol, Quality]])
        result = grid_model.predict(new_data_scaled)

        wine_color = 'Red' if result[0] == 0 else 'White'

        return render_template('home.html', results=wine_color)

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)