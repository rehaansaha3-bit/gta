from sqlalchemy.orm import Session
from database import engine, PlayerMission, Mission


def get_accepted_missions(player_id):

    session = Session(engine)

    accepted = session.query(PlayerMission).filter_by(
        player_id=player_id,
        status="accepted"
    ).all()

    result = []

    for item in accepted:

        mission = session.query(Mission).filter_by(id=item.mission_id).first()

        if mission is not None:
            result.append({
                "mission_id": mission.id,
                "title": mission.title,
                "description": mission.description,
                "difficulty": mission.difficulty,
                "location": mission.location,
                "reward": mission.reward,
                "status": item.status
            })

    session.close()

    return result
