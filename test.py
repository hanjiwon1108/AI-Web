import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("secret.json")
firebase_admin.initialize_app(cred)
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('key', url='https://bssm2-d5365-default-rtdb.firebaseio.com/')
ref.update({"h1":1234})
print(ref.get())