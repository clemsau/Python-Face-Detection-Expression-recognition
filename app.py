# Flask imports
import os

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
        files = pippo = request.form.getlist('name[]')
        print("files: " + files)
        if 'image' in request.files:
            image = request.files['image']
            print("wow: " + str(request.files.filename))
            if image.filename != '':
                image_name = secure_filename(image.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
                image.save(image_path)
                json = DeepFace.analyze(image_path)
        return jsonify(json)
