from flask import Flask, render_template, request, redirect, jsonify, session

# import logging
# import os
import numpy as np
from project.modules import pricePredictor, damageDetector, reduction
import keras
import cv2

app = Flask(__name__)
app.secret_key = "abc"  


# @app.route('/', methods=['GET','POST'])
# def loader():
#     if request.method == 'POST':
#         return redirect("/home")
#     else:
#         return render_template('home.html')    

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':

        files = request.files.getlist('file-input') 
        # print(files)
        if files:
            images = []
            filenames = []
            damage_classes = []
            for file in files:
                if not file.filename:  # Check if filename is empty
                    return render_template('home.html') 

                filename = file.filename  # Get original image name
                filenames.append(filename)
                file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)  
                image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # Load image

                img_str, cat_list = damageDetector(image=image)
                damage_classes.extend(cat_list)

                images.append(img_str)  

            session['damage_classes'] = damage_classes 
        return jsonify(images=images) 

    else:
        return render_template('home.html')     


@app.route('/uploaded', methods=['get'])
def show():
    return render_template('home.html')

@app.route('/features', methods=['POST'])
def handle_form_submissions():
    kilometers_driven = int(request.form['kilometers-driven'])
    mileage = float(request.form['mileage'])
    build_type = request.form['build-type']
    manufacturer = request.form['manufacturer']
    transmission = request.form['transmission']
    fuel_type = request.form['fuel-type']

    user_input_data = {
    'Kilometers_Driven': [kilometers_driven],
    'Mileage': [mileage],
    'Build_Type': [build_type],
    'Manufacturer': [manufacturer], 
    'Transmission': [transmission],
    'Fuel_Type': [fuel_type]
    }

    out = pricePredictor(user_input_data)
    session['price'] = out

    return jsonify({'price': out, 'openModal': True})


@app.route('/final.result')
def get_variable():
    my_variable = reduction(session['price'],session['damage_classes'])  # Replace with your variable generation logic
    return jsonify({'variable': my_variable})

if __name__ == '__main__':
    app.run(debug=True)
