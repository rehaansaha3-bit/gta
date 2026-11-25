
from sqlalchemy.orm import Session
from database import engine, User
from A1 import ph


def create_mission_manager(username, email, password):
    session = Session(engine)

    user_exists = session.query(User).filter_by(email=email).first()

    if user_exists is not None:
        session.close()
        return False

    session.add(User(
        username=username,
        email=email,
        hashed_password=ph.hash(password),
        role="mission_manager"
    ))

    session.commit()
    session.close()

    return True
