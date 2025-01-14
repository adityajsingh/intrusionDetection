from flask import Flask, jsonify, request
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
import time
import urllib.request



cred = credentials.Certificate("E:/IoT J comp/flask_app/apiAPp/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db =  firestore.client()

app = Flask(__name__)

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

firebaseStorage = pyrebase.initialize_app(config)

storage = firebaseStorage.storage()
my_image = "test.jpg"


# importing the twilio library
from twilio.rest import Client

@app.route('/uploadImage', methods=['GET'])
def uploadIMageFirebase():
    auth = firebaseStorage.auth()
    #get url of the image
    email = "hello@gmail.com"
    password = "123456"
    user = auth.sign_in_with_email_and_password(email, password)
    url = storage.child(my_image).get_url(user['idToken'])
    print(url)

    db.collection("device").document("intruderImage").set({'image': url})

        # SID of the twilio account
    twilio_sid = 'YOUR DETAILS' 

    # token id of twilio
    twilio_secret = 'YOUR DETAILS' 

    #my_number represents the number from which the message is to be sent
    my_number = "YOUR DETAILS"

    #other_number is the targerted number which will recieve the message
    other_number = "YOUR DETAILS"

    client = Client(twilio_sid, twilio_secret)

    
    message_twilio = client.messages.create(
    body="Intruder detected please check your phone",
    from_=my_number,
    to=other_number)

    return "uploaded"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
