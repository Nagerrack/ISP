from flask import Flask
from predictor import Predictor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

predictor = Predictor()

@app.route('/get_prediction/<string:sentence>', methods=['GET'])
def get_prediction(sentence):
    return predictor.predict(sentence)

if __name__ == '__main__':
    predictor = Predictor()
    app.run(debug=True)