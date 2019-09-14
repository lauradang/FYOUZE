import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

def create_user_firebase(username,password):
    cred = credentials.Certificate("social-media-app-e8fe0-firebase-adminsdk-qoo7g-55f19c7286.json")
    app = firebase_admin.initialize_app(cred)

    store = firestore.client()
    doc_ref = store.collection(u'users').limit(2)

    doc_ref = store.collection(u'test')

    doc_ref.add(
        {
            u'username': username,
            u'password': password
        }
    )
