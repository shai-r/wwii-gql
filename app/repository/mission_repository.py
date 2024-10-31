from typing import List

from psycopg2 import Error
from sqlalchemy import desc
from returns.maybe import Maybe
from datetime import date

from app.db.database import session_maker
from app.db.models import Mission, Target


def find_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return Maybe.from_optional(
            session.query(Mission).filter(Mission.mission_id == mission_id).first())


def find_missions_by_date_range(start_date: date, end_date: date) -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(
            Mission.mission_date > start_date, Mission.mission_date < end_date
        )

def find_missions_by_targets(targets: List[Target]) -> List[Mission]:
    mission_ids = {t.mission_id for t in targets}
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id.in_(mission_ids)).all()

def find_max_mission_id() -> int:
    with session_maker() as session:
        return session.query(Mission).order_by(desc(Mission.mission_id)).first().mission_id + 1

def create_new_mission(new_mission: Mission):
    with session_maker() as session:
        new_mission.mission_id = find_max_mission_id()
        session.add(new_mission)
        session.commit()
        session.refresh(new_mission)
        return new_mission

def update_mission(mission: Mission):
    with session_maker() as session:
        mission_to_update = session.query(Mission).filter(Mission.mission_id == mission.mission_id).first()
        if not mission_to_update:
            raise Error('not country for this id. SR')
        if mission.mission_date:
            mission_to_update.mission_date = mission.mission_date
        if mission.aircraft_lost:
            mission_to_update.aircraft_lost = mission.aircraft_lost
        if mission.aircraft_failed:
            mission_to_update.aircraft_failed = mission.aircraft_failed
        if mission.airborne_aircraft:
            mission_to_update.airborne_aircraft = mission.airborne_aircraft
        if mission.bombing_aircraft:
            mission_to_update.bombing_aircraft = mission.bombing_aircraft
        if mission.aircraft_returned:
            mission_to_update.aircraft_returned = mission.aircraft_returned
        if mission.attacking_aircraft:
            mission_to_update.attacking_aircraft = mission.attacking_aircraft
        if mission.aircraft_damaged:
            mission_to_update.aircraft_damaged = mission.aircraft_damaged
        session.commit()
        updated = find_mission_by_id(mission.mission_id).unwrap()
        return (mission.mission_date == updated.mission_date or
                mission.aircraft_lost == updated.aircraft_lost or
                mission.aircraft_failed == updated.aircraft_failed or
                mission.bombing_aircraft == updated.bombing_aircraft or
                mission.aircraft_returned == updated.aircraft_returned or
                mission.aircraft_damaged == updated.aircraft_damaged or
                mission.attacking_aircraft == updated.attacking_aircraft or
                mission.airborne_aircraft == updated.airborne_aircraft
                )

def delete_mission(mission_id: int) -> bool:
    with session_maker() as session:
        mission_to_delete = session.query(Mission).filter(Mission.mission_id == mission_id).first()
        if not mission_to_delete:
            raise Error('not mission for this id. SR')
        session.delete(mission_to_delete)
        session.commit()
    deleted = find_mission_by_id(mission_id).value_or(None) is None
    return deleted
