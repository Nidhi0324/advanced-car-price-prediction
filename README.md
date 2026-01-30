# Advanced Car Price Prediction Model

An end-to-end machine learning system that predicts the market value of a used car and dynamically adjusts the price based on image-based damage detection. The project integrates traditional machine learning, deep learning (computer vision), and a Flask-based web application to deliver a transparent and user-friendly car valuation experience.

## Project Overview

Selling or buying a used car often involves uncertainty around fair pricing and hidden damages. This project solves that problem by combining tabular machine learning for base car price prediction with YOLO-based computer vision for detecting physical car damages from uploaded images. A rule-based price adjustment mechanism then modifies the predicted price based on detected damages. The entire pipeline is wrapped in an interactive Flask web application.

## Key Features

- Predicts used car prices using features such as mileage, kilometers driven, fuel type, transmission, manufacturer, and build type  
- Detects multiple types of car damages from uploaded images using a deep learning model  
- Dynamically adjusts car price based on detected damages  
- Interactive web interface with real-time predictions  
- Modular backend design for easy extension and maintenance  

## Tech Stack

Backend and Machine Learning:
Python, Scikit-learn, Pandas, NumPy, TensorFlow, Keras, OpenCV, YOLO

Web Application:
Flask, HTML, CSS, JavaScript

Tools:
Jupyter Notebook, GitHub, Google Drive (for hosting large model files)

## Project Structure

advanced-car-prdiction-model/
├── app/
│   ├── backend/
│   │   ├── app.py
│   │   ├── model_utils.py
│   │   └── yolo_utils.py
│   └── frontend/
│       ├── index.html
│       ├── upload.html
│       ├── style.css
│       ├── main.js
│       ├── favicon.ico
│       └── search_icon.png
├── models/
│   ├── preprocessing_pipeline.pkl
│   └── README.md
├── notebooks/
│   └── 01_car_price_prediction.ipynb
├── docs/
│   ├── project_report.pdf
│   ├── project_poster.pdf
│   └── project_presentation.pptx
└── README.md

## Model Files

Due to GitHub file size limitations, trained model files are not included directly in this repository.

Required model files:
- car_price_model.sav – trained regression model for car price prediction  
- damage_detection_yolo.h5 – YOLO-based damage detection model  

Download trained models from Google Drive:
https://drive.google.com/drive/folders/1uVa9jD_-Ky9Rtu-B0DwdCHp9zh6dkXP4?usp=sharing

After downloading, place both model files inside the models/ directory.

## How the System Works

1. The user enters car details such as mileage, kilometers driven, fuel type, and transmission  
2. The machine learning model predicts the base price of the car  
3. The user optionally uploads car images  
4. The YOLO-based damage detection model identifies visible damages  
5. The system applies damage-based price reduction logic  
6. The final adjusted car price is displayed to the user  

## How to Run the Project Locally

Clone the repository:
git clone https://github.com/Nidhi0324/advanced-car-price-prediction

Install dependencies:
pip install -r requirements.txt

Download model files:
Download the trained models from the Google Drive link and place them inside the models/ folder.

Run the Flask application:
python app/backend/app.py

Open the application in your browser:
http://127.0.0.1:5000

## Notebook

The notebook 01_car_price_prediction.ipynb contains data preprocessing, feature engineering, model training, and evaluation for the car price prediction model.

## Documentation

The docs folder contains the full project report, project poster, and final presentation slides describing the methodology, system design, results, and future scope.

## Future Enhancements

- Upgrade to newer YOLO versions such as YOLOv7 or YOLOv8  
- Train on larger and more diverse datasets  
- Add user authentication and prediction history  
- Deploy the application using Docker and cloud platforms  
- Provide analytics on damage-based and regional price trends  

## Final Note

This project demonstrates a complete end-to-end applied machine learning pipeline, combining structured data modeling, computer vision, and full-stack deployment. It is designed to be modular, extensible, and portfolio-ready.
