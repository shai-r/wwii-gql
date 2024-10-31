from typing import List

import toolz
from returns.maybe import Maybe
from datetime import date
from psycopg2 import Error

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
        return session.query(Mission).filter(max(Mission.mission_id)) + 1

def create_new_mission(new_mission: Mission):
    with session_maker() as session:
        new_mission.mission_id = find_max_mission_id()
        session.add(new_mission)
        session.commit()
        return new_mission

# def update_country(country: Country):
#     with session_maker() as session:
#         if country.id is None:
#             raise Error('No country ID. Which country do you need to update? SR')
#         country_to_update = session.query(Country).filter(Country.id == country.id).first()
#         if not country_to_update:
#             raise Error('not country for this id. SR')
#         if country.name:
#             country_to_update.name = country.name
#         if country.region:
#             country_to_update.region = country.region
#         if country.capital:
#             country_to_update.capital = country.capital
#         session.commit()
#         updated = find_country_by_id(country.id)
#         return (country.name == updated.name or
#                 country.region == updated.region or
#                 country.capital == updated.capital)
#
# def delete_country(country_id: int):
#     with session_maker() as session:
#         country_to_delete = session.query(Country).filter(Country.id == country_id).first()
#         if not country_to_delete:
#             raise Error('not country for this id. SR')
#         session.delete(country_to_delete)
#         session.commit()
#         deleted = find_country_by_id(country_id) is None
#         return deleted
