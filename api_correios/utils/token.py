import jwt
from datetime import datetime

def token_is_expired(token: str) -> bool:
    decoded_token = jwt.decode(token, options={'verify_signature': False})

    expiration_timestamp = decoded_token['exp']
    now_timestamp = datetime.timestamp(datetime.now())

    if now_timestamp >= expiration_timestamp:
        return True
    return False
