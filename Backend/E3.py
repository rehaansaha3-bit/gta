
from sqlalchemy.orm import Session
from database import engine, Mission


def get_available_missions():

    session = Session(engine)

    missions = session.query(Mission).filter_by(is_available=1).all()

    result = []

    for mission in missions:
        result.append({
            "id": mission.id,
            "title": mission.title,
            "description": mission.description,
            "difficulty": mission.difficulty,
            "location": mission.location,
            "reward": mission.reward
        })

    session.close()

    return result
