from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Convolution2D, MaxPooling2D, Flatten

from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range =0.2, zoom_range =0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)

x_train = train_datagen.flow_from_directory(r'E:/IoT J comp/ML_model/train_set',target_size = (64,64),batch_size = 32,class_mode = "categorical")
x_test = test_datagen.flow_from_directory(r'E:/IoT J comp/ML_model/test_set',target_size = (64,64),batch_size = 32,class_mode = "categorical")


model=Sequential()
model.add(Convolution2D(32,(2,2),input_shape = (64,64,3)))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(kernel_initializer='uniform',activation='relu',units=300))
model.add(Dense(kernel_initializer='uniform',activation='relu',units=100))
model.add(Dense(kernel_initializer='uniform',activation='relu',units=60))
model.add(Dense(units = 3, kernel_initializer="random_uniform",activation="softmax"))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',metrics=["accuracy"])

model.fit_generator(x_train,steps_per_epoch = len(x_train),
                    epochs=40,
                    validation_data=x_test,
                    validation_steps = len(x_test))

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('E:/IoT J comp/ML_model/train_set/human/pexels-photo-614810.jpeg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
x_train.class_indices
if result[0][0] == 1:
    prediction = 'Cow'
elif result[0][1] == 1:
    prediction = 'elephant'
elif result[0][2] == 1:
    prediction = 'human'
    
   
print(result)
print(prediction)

model.save('animal_custom.h5')
