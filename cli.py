"""lol
"""
import pyrebase

from firebase_config import (
    FIREBASE_CONFIG as conf, 
    CREDENTIALS as cred,
)

firebase = pyrebase.initialize_app(conf)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password(cred.get('email'), cred.get('password'))

