import os

import firebase_admin
from firebase_admin import credentials, firestore

from doc_lms.settings import BASE_DIR

cred = credentials.Certificate(os.path.join(BASE_DIR / 'serviceAccountKey.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()

