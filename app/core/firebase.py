import os
import json
import firebase_admin
from firebase_admin import credentials, auth

# Load credentials from environment variable
firebase_json = os.getenv("FIREBASE_CREDENTIALS")
if not firebase_json:
    raise RuntimeError("FIREBASE_CREDENTIALS not set")

cred = credentials.Certificate(json.loads(firebase_json))

# Initialize Firebase app
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def get_user_role(token: str) -> str:
    decoded = auth.verify_id_token(token)
    return decoded.get("role", "user")
