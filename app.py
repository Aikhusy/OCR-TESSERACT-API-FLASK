import numpy
from flask import Flask, request, jsonify
import cv2
import pytesseract
import re
from preprocessing import preprocessing
from regex import idRegex

app = Flask(__name__)

@app.route('/extract_info', methods=['POST'])
def extract_info():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    image = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)

    ready=preprocessing(image)

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    text = pytesseract.image_to_string(ready)


    result=idRegex(text)

    return jsonify(result)

if __name__ == '__main__':
    app.run('0.0.0.0' ,debug=True)