import firebase_admin
from firebase_admin import credentials, db
from firebase import firebase

def create_user_firebase(username):
    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")
    app.put('users',username,{'fb_link':''})