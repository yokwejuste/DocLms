import firebase_admin
import jsonpickle as jsonpickle
from firebase_admin import credentials, firestore

from doc_lms.settings import firebase_admin_config_credentials

cred = credentials.Certificate(jsonpickle.encode(firebase_admin_config_credentials))
firebase_admin.initialize_app(cred)

db = firestore.client()
