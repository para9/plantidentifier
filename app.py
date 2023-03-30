import tensorflow as tf
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from io import BytesIO
from PIL import Image
from fuzzywuzzy import process


app = Flask(__name__)

# Load the new model
new_model = tf.keras.models.load_model('/home/kunal/workspace/flask/my_model.h5')

# Load the preprocessed features
preprocessed_features = np.load('/home/kunal/workspace/flask/preprocessed_features.npy')

# Load the plant details data
plant_details = pd.read_excel('/home/kunal/Downloads/Plant name and properties.xlsx')

EXPECTED_SHAPE = (1200, 900, 3)

def preprocess_image(input_data):
    # Load and preprocess the image data here
    img = Image.open(input_data).resize((224, 224))
    img = np.array(img) / 255.0  # normalize pixel values
    img = np.expand_dims(img, axis=0)  # add batch dimension
    img = tf.keras.applications.resnet50.preprocess_input(img)  # apply ResNet50 preprocessing
    img = np.expand_dims(img, axis=1)  # add height dimension
    img = np.expand_dims(img, axis=1)  # add width dimension
    return img


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/plant_identifier')
def plant_identifier():
    return render_template('identifier.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.files['imagefile']
        print(input_data)
        img = Image.open(BytesIO(input_data.read()))
        img = preprocess_image(img)
        prediction = new_model.predict(img)
        predicted_plant = plant_details.iloc[np.argmax(prediction)]['Common Name']
        plant_score = np.max(prediction) * 100
        closest_match, score = process.extractOne(predicted_plant, plant_details['Common Name'], scorer=fuzz.token_sort_ratio)
        plant_info = plant_details.loc[plant_details['Common Name'] == closest_match]
        plant_dict = plant_info.to_dict('records')[0]
        result = {'prediction': prediction.tolist(), 'plant_info': plant_dict, 'similarity_score': score, 'plant_score': plant_score}
        return render_template('identifier.html', prediction=result['prediction'], plant_info=result['plant_info'],  similarity_score=result['similarity_score'], plant_score=result['plant_score'])
    except Exception as e:
        print(e)
        return render_template('error.html')
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error='Page not found'), 404




@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

if __name__=='__main__':
    app.run(port = 3001, debug=True)

