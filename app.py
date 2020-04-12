# Flask imports
import os
import base64
import uuid

from flask import Flask, request, jsonify, render_template
from config import SECRET_KEY, UPLOAD_PATH, TEMPLATE_FOLDER
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
app.config['TEMPLATE_FOLDER'] = TEMPLATE_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        json = {}
        if 'image' in request.form:
            image = request.form['image']
            image = base64.b64decode(image)
            print("wow: " + str(request.files.filename))
            image_name = uuid.uuid4().hex + '.jpg'
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            with open(image_path, 'wb') as f:
                f.write(image)
            json = DeepFace.analyze(image_path)
        return jsonify(json)
