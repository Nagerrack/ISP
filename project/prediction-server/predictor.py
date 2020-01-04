from keras.models import model_from_json
import tensorflow_hub as hub
import tensorflow as tf
import logging
import numpy as np
from nn import NeuralNetwork
from keras_preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
import json


class Predictor():

    MODEL_WEIGHTS = 'prediction-server/model/model.h5'
    MODEL_ARCH = 'prediction-server/model/model.json'
    TOKENIZER = 'prediction-server/model/tokenizer.json'

    MAX_NAME_SEQ = 10
    MAX_ITEM_DESC_SEQ = 75

    def __init__(self):
        self.logger = logging.getLogger('predictor.Predictor')
        self.nn = NeuralNetwork()
        with open(self.TOKENIZER, 'r') as f:
            self.tokenizer = tokenizer_from_json(f.read())
        self.nn.load([self.MODEL_ARCH, self.MODEL_WEIGHTS])

    def predict(self, data):
        prepared_data = self.prepare_data(data)
        prediction = self.nn.predict(prepared_data)[0]
        price = self.prediction_to_price(prediction)
        return price

    def prediction_to_price(self, prediction):
        scale = 0.26295411
        minimum = -1
        prediction -= minimum
        prediction /= scale
        return np.exp(prediction)+1

    def prepare_data(self, data):
        name = pad_sequences(self.tokenizer.texts_to_sequences(
            [data["name"].lower()]), self.MAX_NAME_SEQ)
        description = pad_sequences(self.tokenizer.texts_to_sequences(
            [data["description"].lower()]), self.MAX_ITEM_DESC_SEQ)
        brand_name = [0]  # TODO
        category = [0]  # TODO
        item_condition = [data["itemCondition"]]  # TODO
        shipping = [data["shipping"]]  # TODO
        return {
            'name': name, 
            'item_desc': description, 
            'brand_name': np.array(brand_name), 
            'category_name': np.array(category), 
            'item_condition': np.array(item_condition), 
            'num_vars': np.array(shipping)
        }