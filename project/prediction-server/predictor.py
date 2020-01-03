from keras.models import model_from_json
import tensorflow_hub as hub
import tensorflow as tf
import logging
import numpy as np
from nn import NeuralNetwork
from keras_preprocessing.text import tokenizer_from_json
import json

class Predictor():

    MODEL_WEIGHTS = 'prediction-server/model/model.h5'
    MODEL_ARCH = 'prediction-server/model/model.json'
    TOKENIZER = 'prediction-server/model/tokenizer.json'

    def __init__(self):
        self.logger = logging.getLogger('predictor.Predictor')
        self.nn = NeuralNetwork()
        with open(self.TOKENIZER, 'r') as f:
            self.tokenizer = tokenizer_from_json(f.read())
        self.nn.load([self.MODEL_ARCH, self.MODEL_WEIGHTS])

    def predict(self, data):
        return data

    def tokenize(self, data):
        pass