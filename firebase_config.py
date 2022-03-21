import os

import firebase_admin
from firebase_admin import credentials, firestore

from doc_lms.settings import BASE_DIR

cred = credentials.Certificate(os.path.join(BASE_DIR / 'serviceAccountKey.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('users').document().collection('user1').document('user1').set(
    {'name': {'first_name': 'Yorker', 'second_name': 'Steve'}, 'email': 'me@gmail.com'})
