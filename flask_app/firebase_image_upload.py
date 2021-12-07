import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db =  firestore.client()


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
my_image = "image.jpeg"

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

    db.collection("device").document("intruderImage").set({'image': url})

upload_the_image()