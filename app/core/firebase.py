import json
import firebase_admin
from firebase_admin import credentials, auth, exceptions as firebase_exceptions
from dotenv import load_dotenv
from app.core.config import settings  # Use Pydantic settings

# Load environment variables
load_dotenv()

# Load Firebase credentials from environment
firebase_json = settings.FIREBASE_CREDENTIALS
if not firebase_json:
    raise RuntimeError("FIREBASE_CREDENTIALS not set")

# Parse and initialize Firebase app
cred = credentials.Certificate(json.loads(firebase_json))
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Extract user role from token
def get_user_role(token: str) -> str:
    decoded = verify_token(token)
    return decoded.get("role", "user")

# Verify Firebase ID token
def verify_token(token: str) -> dict:
    try:
        return auth.verify_id_token(token)
    except firebase_exceptions.FirebaseError as e:
        raise RuntimeError(f"Token verification failed: {e}")
