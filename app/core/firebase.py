import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("firebase-admin.json")
firebase_admin.initialize_app(cred)

def verify_token(token: str):
    return auth.verify_id_token(token)

def get_user_role(token: str) -> str:
    try:
        decoded = verify_token(token)
        return decoded.get("role", "user")
    except Exception:
        return "unauthorized"
