from flask import Flask, request, jsonify
import numpy as np
import joblib

app   = Flask(__name__)
model = joblib.load('linear_regression_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():

    data        = request.json
    values      = [data['plot_size']]
    X           = np.array(values).reshape(1, -1)
    prediction  = model.predict(X)
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(debug=False)
