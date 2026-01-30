import pandas as pd
# import sklearn
import random
import tensorflow as tf
# import numpy as np
from base_root import *
import base64
import pickle


convertor = {
    'Build_Type': {'Minivans': 1, 'Hatchback': 2, 'Sedan': 3, 'MUV': 4, 'Other': 5, 'Luxury Vehicles': 6, 'SUV': 7},
    'Transmission': {'Manual': 1, 'Automatic': 2}, 
    'Fuel_Type': {'LPG': 1, 'CNG': 2, 'Petrol': 3, 'Diesel': 4, 'Electric': 5}, 
    'Manufacturer': {'Chevrolet': 1, 'Fiat': 2, 'Datsun': 3, 'Nissan': 4, 'Maruti': 5, 'Renault': 6, 'Volkswagen': 7,'Ford': 8,
                        'Honda': 9, 'Hyundai': 10, 'Tata': 11, 'Skoda': 12, 'Mitsubishi': 13, 'Mahindra': 14, 'Toyota': 15, 'Kia': 16,
                        'Volvo': 17, 'BMW': 18, 'Jeep': 19, 'Mercedes-Benz': 20, 'Audi': 21, 'Other': 22, 'MG': 23, 'Jaguar': 24}
}


def pricePredictor(new_data, convertor=convertor):
    loaded_model = pickle.load(open("C:/Users/RutulPatel/Jupyter/car_price_model_1.sav", 'rb'))
    loaded_pipe = pickle.load(open("C:/Users/RutulPatel/Jupyter/preprocess_pipe.pkl", 'rb'))

    for i in new_data: 
        item = new_data[i][0]
        if isinstance(item,str):
            new_data[i][0] = convertor[i][item]
    

    processed_df = pd.DataFrame(new_data)
    processed_df = pd.DataFrame(loaded_pipe.transform(processed_df), columns=['Kilometers_Driven', 'Mileage', 'Build_Type', 'Transmission','Fuel_Type', 'Manufacturer'])
    # print('Processed df:\n',processed_df)
    predictions = (loaded_model.predict(processed_df))
    # print(predictions)
    predictions = (round(float(predictions*100))/100)
    return (predictions)


def damageDetector(image):
    def mish(x):
        return x * tf.math.tanh(tf.math.softplus(x)) 
    model = keras.models.load_model(base_path()+'Jupyter/IPYNB/best_model_trained_yet.h5', custom_objects={"mish": mish})
    net_h, net_w = 416, 416
    obj_thresh, nms_thresh = 0.45, 0.1
    anchors = [[116,90,  156,198,  373,326],  [30,61, 62,45,  59,119], [10,13,  16,30,  33,23]]
    labels = ["Bonnet-Damage", "Boot-Damage", "Door-Outer-Dent", "Fender-Dent", "Front-Bumper-Dent", "Front-WindScreen-Damage",\
          "HeadLight-Damage", "QuarterPanel-Dent", "Rear-Bumper-Dent", "Rear-WindScreen-Damage", "Roof-Dent", "RunningBoard-Dent",\
          "SideMirror-Damage", "TailLight-Damage"]
    # anchors = [[75, 50, 102,118, 175, 69], [191,166, 127,251, 278,115], [326,201, 220,301, 367,319]]
    image_h, image_w, _ = image.shape
    new_image = preprocess_input(image, net_h, net_w)

    # running the prediction
    yolos = model.predict(new_image)
    boxes = []

    for i in range(len(yolos)):
        # decode the output of the network
        boxes += decode_netout(yolos[i][0], anchors[i], obj_thresh, nms_thresh, net_h, net_w)

    # correct the sizes of the bounding boxes
    correct_yolo_boxes(boxes, image_h, image_w, net_h, net_w)

    # suppress non-maximal boxes
    do_nms(boxes, nms_thresh)

    # draw bounding boxes on the image using labels
    image, cat_list = draw_boxes(image, boxes, labels, obj_thresh) 
    # print(cat_list)
    _, img_encoded = cv2.imencode('.jpg', image)  # Encode as JPEG 
    img_str = base64.b64encode(img_encoded.tobytes()).decode()
    return img_str, cat_list


def reduction(price, damage_categories):
    damage_categories = set(damage_categories)

    damage_reduction_map = {
        "Bonnet-Damage": 4.5,
        "Boot-Damage": 4.5,
        "Door-Outer-Dent": 2.5,  
        "Fender-Dent": 2.5,  
        "Front-Bumper-Dent": 3,
        "Front-WindScreen-Damage": 6,
        "HeadLight-Damage": 5.5,  
        "QuarterPanel-Dent": 4,
        "Rear-Bumper-Dent": 3,
        "Rear-WindScreen-Damage": 6,
        "Roof-Dent": 4.5,  
        "RunningBoard-Dent": 1.5, 
        "SideMirror-Damage": 3,  
        "TailLight-Damage": 4
    }

    print(damage_categories)
    total_reduction = 0
    num_damages = len(damage_categories)

    exponential_factor = 1.036
    division_factor = exponential_factor ** num_damages

    for damage in damage_categories:
        if damage in damage_reduction_map:
            base_reduction = damage_reduction_map[damage]*0.9
            offset_range = 0.1 * base_reduction  # 5% of original value
            offset = random.uniform(-offset_range, offset_range) 
            # print(offset) 
            adjusted_reduction = base_reduction + offset
            total_reduction += adjusted_reduction
    
    print(total_reduction)
    adjusted_total_reduction = total_reduction / division_factor
    print("adjusted_total_reduction",adjusted_total_reduction)
    capped_adjusted_reduction = min(30, adjusted_total_reduction)  # Keep 30% max cap
    adjusted_price = price * (100 - capped_adjusted_reduction)/100
    adjusted_price = (round(adjusted_price*100)/100)
    print(adjusted_price)
    return adjusted_price



# reduction(523718.14,["Bonnet-Damage", "Boot-Damage",])





user_input_data = {
    'Kilometers_Driven': [50000,2356],
    'Mileage': [25,12],
    'Build_Type': ['Sedan','SUV'],
    'Manufacturer': ['Honda','BMW'], 
    'Transmission': ['Manual','Manual'],
    'Fuel_Type': ['Diesel','LPG']
    }
# print(user_input_data.keys())
# # pricePredictor(user_input_data)