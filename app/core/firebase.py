import json
import firebase_admin
from firebase_admin import credentials, auth, exceptions as firebase_exceptions
from dotenv import load_dotenv
from app.core.config import settings  # Pydantic settings object

# ✅ Load environment variables (for local dev)
load_dotenv()

# ✅ Load Firebase credentials from environment
firebase_json = settings.FIREBASE_CREDENTIALS
if not firebase_json:
    raise RuntimeError("FIREBASE_CREDENTIALS not set")

# ✅ Parse and initialize Firebase app
try:
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
except json.JSONDecodeError as e:
    raise RuntimeError(f"Invalid FIREBASE_CREDENTIALS format: {e}")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# ✅ Verify Firebase ID token
def verify_token(token: str) -> dict:
    try:
        return auth.verify_id_token(token)
    except firebase_exceptions.FirebaseError as e:
        raise RuntimeError(f"Token verification failed: {e}")

# ✅ Extract user role from token
def get_user_role(token: str) -> str:
    decoded = verify_token(token)
    return decoded.get("role", "user")
