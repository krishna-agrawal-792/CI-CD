from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model('model/diabetic_retinopathy_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    img_file = request.files['file']
    img = image.load_img(img_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.

    prediction = model.predict(img_array)
    result = {'Normal': float(prediction[0][0]), 'Diabetic Retinopathy': float(prediction[0][1])}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
