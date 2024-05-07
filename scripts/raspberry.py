import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/home/pic/Desktop/Firebase/pic24-cfe9a-firebase-adminsdk-mddbb-f4b6592437.json")
firebase_admin.initialize_app(cred)


# Initialize Firestore
db = firestore.client()

# Add a new document with a generated ID
doc_ref = db.collection(u'users').document()
doc_ref.set({
    u'first_name': u'Vasco',
    u'last_name': u'Martins',
    u'age': 90
})

print("Document added with ID:", doc_ref.id)

