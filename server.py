from flask import Flask, request, Response
import tensorflow.keras
import jsonpickle
from PIL import Image, ImageOps
import numpy as np
import os

model = tensorflow.keras.models.load_model('model/keras_model.h5', compile=False)
labelsFile = "model/labels.txt"
labels = []

with open(labelsFile, 'r') as File:
	infoFile = File.readlines()
	for line in infoFile:
		words = line.split()
		labels.append(words[1])	# Second position is the label

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello world!"

@app.route('/predict', methods=['POST'])
def predict_req():
	imagefile = request.files.get('imagefile', '')

	np.set_printoptions(suppress = True)

	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

	image = Image.open(imagefile)

	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	image_array = np.asarray(image)
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

	data[0] = normalized_image_array
	predictions = model.predict(data)

	label_index = np.argmax(predictions[0])
	return labels[label_index]
	#return labels[0] + " proba: " + str(predictions[0][0]) + "\n" + labels[0] + " proba: " + str(predictions[0][1])

if __name__ == '__main__':
	app.run(port=5000)