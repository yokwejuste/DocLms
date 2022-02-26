import pyrebase

from doc_lms.settings import env

config = {
    "apiKey": env("F_API"),
    "authDomain": env("F_AUTH_DOMAIN"),
    "databaseURL": env("F_DATABASE_URL"),
    "projectId": env("F_PROJECT_ID"),
    "storageBucket": env("F_STORAGE_BUCKET"),
    "messagingSenderId": env("F_MESSAGING_SENDER_ID"),
    "appId": env("F_APP_ID"),
    "measurementId": env("F_MEASUREMENT_ID")
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
