import os
from doc_lms.settings import BASE_DIR
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(os.path.join(BASE_DIR / 'school/serviceAccountKey.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()

