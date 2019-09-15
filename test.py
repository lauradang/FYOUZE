import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("social-media-app-e8fe0-firebase-adminsdk-qoo7g-55f19c7286.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://social-media-app-e8fe0.firebaseio.com/'
})

ref = db.reference('/')

# users_ref = ref.child('users')
# users_ref.set({
#     'oliviabuttholexie': {
#         'date_of_birth': 'feb 69, 420',
#         'full_name': 'Olivia the monkey Xie'
#     }
# })

ref.set(
    {
        "users": {
                "lauradang": {
                    "fb_link": "https://www.facebook.com/lauradang04"
                } 
            }
    }
)