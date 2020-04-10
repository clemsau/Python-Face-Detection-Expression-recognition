# Flask imports
import os

from flask import Flask,  request, jsonify
from config import SECRET_KEY, UPLOAD_PATH
from werkzeug.utils import secure_filename

# Classifier imports
from deepface import DeepFace
import cv2
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return UPLOAD_PATH + "index.html"
    if request.method == 'POST':
        json = {}
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                image_name = secure_filename(image.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
                image.save(image_path)
                json = DeepFace.analyze(image_path)
        return jsonify(json)
