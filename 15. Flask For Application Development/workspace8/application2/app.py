import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
from pycaret.regression import *

app = Flask(__name__)

model = load_model('deployment_28042020')
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        int_features = [x for x in request.form.values()]
        final = np.array(int_features).reshape(1, -1)
        data_unseen = pd.DataFrame(final, columns=cols)
        prediction = predict_model(model, data=data_unseen, round=0)
        output = prediction.iloc[0, prediction.columns.get_loc('Label')]
        return render_template('home.html', pred='Expected Bill will be {}'.format(output))
    except Exception as e:
        return render_template('home.html', pred='Error: {}'.format(str(e)))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.get_json(force=True)
        data_unseen = pd.DataFrame([data])
        prediction = predict_model(model, data=data_unseen)
        output = prediction.iloc[0, prediction.columns.get_loc('Label')]
        return jsonify(output)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



