from sqlalchemy.orm import Session
from database import engine, PlayerMission


def submit_completion(player_id, mission_id, completion_details):

    session = Session(engine)

    mission = session.query(PlayerMission).filter_by(
        player_id=player_id,
        mission_id=mission_id,
        status="accepted"
    ).first()

    if mission is None:
        session.close()
        return False

    mission.completion_details = completion_details
    mission.status = "pending"

    session.commit()
    session.close()

    return True