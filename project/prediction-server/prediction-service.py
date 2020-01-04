from flask import Flask, request, jsonify
from predictor import Predictor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

predictor = Predictor()

@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    data = request.json
    price = predictor.predict(data)[0]
    return jsonify({'price': float(price)})


if __name__ == '__main__':
    predictor = Predictor()
    app.run(debug=True)