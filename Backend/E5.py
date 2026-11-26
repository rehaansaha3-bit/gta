
from sqlalchemy.orm import Session
from database import engine, Mission, PlayerMission


def accept_mission(player_id, mission_id):

    session = Session(engine)

    mission = session.query(Mission).filter_by(id=mission_id).first()

    if mission is None:
        session.close()
        return "not_found"

    if mission.is_available == 0:
        session.close()
        return "unavailable"

    already_accepted = session.query(PlayerMission).filter_by(
        player_id=player_id,
        mission_id=mission_id,
        status="accepted"
    ).first()

    if already_accepted is not None:
        session.close()
        return "already_accepted"

    new_mission = PlayerMission(
        player_id=player_id,
        mission_id=mission_id,
        status="accepted"
    )
    # used it to save the data in database
    session.add(new_mission)
    session.commit()
    session.close()

    return True
