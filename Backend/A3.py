
import os
from datetime import datetime, timedelta, timezone
import jwt
from sqlalchemy.orm import Session
from database import engine, User

ACCESS_TOKEN_EXPIRY = 15
REFRESH_TOKEN_EXPIRY = 7 * 24 * 60
SECRET_KEY = os.getenv("SECRET_KEY") or "local-dev-key"
# instead of using secret key directly, it is better to use environment variables for security reasons.
ALGORITHM = "HS256"


def create_token(email, token_type):
    time = ACCESS_TOKEN_EXPIRY

    if token_type == "refresh":
        time = REFRESH_TOKEN_EXPIRY

    payload = {
        "email": email,
        "token_type": token_type,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=time)
    }

    token = jwt.encode(
        payload=payload,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token, token_type):
    try:
        payload = jwt.decode(
            jwt=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except:
        return False

    if payload["token_type"] == token_type:
        return payload["email"]

    return False


def get_user_id(email):
    session = Session(engine)

    user = session.query(User).filter_by(email=email).first()

    if user is None:
        session.close()
        return None

    user_id = user.id

    session.close()
    return user_id


def refresh_access_token(refresh_token):
    email = verify_token(
        token=refresh_token,
        token_type="refresh"
    )

    if not email:
        return False

    return create_token(email=email, token_type="access")
