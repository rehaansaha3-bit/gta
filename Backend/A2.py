
from sqlalchemy.orm import Session
from argon2.exceptions import VerifyMismatchError
from database import engine, User
from A1 import ph
import A3 


def verify_login(email, password):
    session = Session(engine)

    user = session.query(User).filter_by(email=email).first()

    if user is None:
        session.close()
        return False

    try:
        ph.verify(user.hashed_password, password)
    except VerifyMismatchError:
        session.close()
        return False

    session.close()

    access_token = A3.create_token(email=email, token_type="access")
    refresh_token = A3.create_token(email=email, token_type="refresh")

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
