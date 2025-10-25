from pydantic import BaseModel

class MpesaCallback(BaseModel):
    Body: dict
