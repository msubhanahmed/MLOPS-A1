from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('linear_regression_model.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    data = request.json
    if 'plot_size' not in data:
        return jsonify({'error': 'Invalid JSON.'}), 400
    try:
        plot_size = float(data['plot_size'])
    except ValueError:
        return jsonify({'error': 'Invalid plot_size value.'}), 400

    X = np.array([[plot_size]])
    prediction = model.predict(X)
    return jsonify({'predicted_price': prediction[0]})


if __name__ == '__main__':
    app.run(debug=False)
