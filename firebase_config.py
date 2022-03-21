import firebase_admin
from firebase_admin import credentials, firestore

from doc_lms.settings import firebase_admin_config_credentials

cred = credentials.Certificate(firebase_admin_config_credentials)
firebase_admin.initialize_app(cred)

db = firestore.client()
