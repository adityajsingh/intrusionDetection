#this  python script contains the code to predicting whether it
# the picture taken of the subject is potential threat or no

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import twilioMessage



model = load_model('animal_custom.h5')



def predict_Instrusion(image_path):
    img = image.load_img(image_path, target_size=(64,64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)

    print('prediction: ', preds)

    index = ['Cow', 'elepant', 'Human']

    print(np.argmax(preds))

    text = str(index[np.argmax(preds)])


    if np.argmax(preds) != 2:
        send_message("A wild animal is spotted\ncheck your app to know more")



predict_Instrusion('E:/IoT J comp/ML_model/train_set/human/pexels-photo-614810.jpeg')