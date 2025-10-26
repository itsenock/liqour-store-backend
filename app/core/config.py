from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    STRIPE_SECRET_KEY: str
    STRIPE_SUCCESS_URL: str = "https://your-frontend.com/success"
    STRIPE_CANCEL_URL: str = "https://your-frontend.com/cancel"
    LIQUOR_API_URL: str
    LIQUOR_API_KEY: str
    MPESA_CONSUMER_KEY: str
    MPESA_CONSUMER_SECRET: str
    MPESA_SHORTCODE: str
    MPESA_PASSKEY: str
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str
    SENDGRID_API_KEY: str
    SENDGRID_FROM_EMAIL: str
    FIREBASE_CREDENTIALS: str

    class Config:
        env_file = ".env"

settings = Settings()
