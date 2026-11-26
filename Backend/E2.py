
from sqlalchemy.orm import Session
from database import engine, Mission


def create_mission(title, description, difficulty, location, reward, manager_id):

    session = Session(engine)

    mission = Mission(
        title=title,
        description=description,
        difficulty=difficulty,
        location=location,
        reward=reward,
        manager_id=manager_id
    )

    session.add(mission)
    session.commit()

    mission_id = mission.id

    session.close()

    return mission_id
