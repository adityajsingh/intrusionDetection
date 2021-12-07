import RPi.GPIO as GPIO
from  time import sleep
import picamera
#import firebase_image_upload
#import model_predict
#import twilioMessage

import pyrebase
#import firebase_admin
#from firebase_admin import credentials, firestore

#cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred)

#db =  firestore.client()


config = {
  'apiKey': "YOUR DETAILS",
  'authDomain': "YOUR DETAILS",
  'projectId': "YOUR DETAILS",
  'storageBucket': "YOUR DETAILS",
  'messagingSenderId': "YOUR DETAILS",
  'appId': "YOUR DETAILS",
  'measurementId': "YOUR DETAILS",
  "serviceAccount": "serviceAccountKey.json",
  "databaseURL": "YOUR DETAILS"
}

GPIO.setmode(GPIO.BCM)



pirPin = 26

GPIO.setup(pirPin, GPIO.IN)

print("Starting Motion Detection")

sleep(.2)
sm = 0


firebaseStorage = pyrebase.initialize_app(config)

storage = firebaseStorage.storage()
my_image = "test.jpg"

def upload_the_image():
    #uplod the image
    storage.child(my_image).put(my_image)
    auth = firebaseStorage.auth()
    #get url of the image
    email = "hello@gmail.com"
    password = "123456"
    user = auth.sign_in_with_email_and_password(email, password)
    url = storage.child(my_image).get_url(user['idToken'])
    print(url)

def MOTION(pirPin):
	print("Motion is detected")
	
	
	print("About to capture an Image")
	#sleep(10)
	with picamera.PiCamera() as camera:
		camera.resolution = (1280,720)
		camera.capture("/home/pi/Desktop/iotJComp-main/test.jpg")
	print("Picture taken.")
	
	print("Uploading Picture")
	upload_the_image()
	

try:
	print("PIR Module Test (CTRL+C to exit)")
	sleep(2)
	print("Ready")
	GPIO.add_event_detect(pirPin, GPIO.RISING, callback=MOTION)
	while True:
		sm+=1
		print(sm)
		sleep(10)
except keyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
