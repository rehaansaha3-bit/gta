from sqlalchemy.orm import Session
from database import engine, Mission


def get_mission_by_id(mission_id):

    session = Session(engine)

    mission = session.query(Mission).filter_by(id=mission_id).first()

    if mission is None:
        session.close()
        return None

    result = {
        "id": mission.id,
        "title": mission.title,
        "description": mission.description,
        "difficulty": mission.difficulty,
        "location": mission.location,
        "reward": mission.reward,
        "manager_id": mission.manager_id,
        "is_available": mission.is_available
    }

    session.close()

    return result
