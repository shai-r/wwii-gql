from typing import  List
from returns.maybe import Maybe
from psycopg2 import Error

from app.db.database import session_maker
from app.db.models import Mission
from app.utils.date_utils import is_date_in_date_range


def find_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()

def find_missions_by_date_range(start_date: str, end_date: str) -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(is_date_in_date_range(str(Mission.mission_date), start_date, end_date))


# def create_new_country(new_country: Country):
#     with session_maker() as session:
#         session.add(new_country)
#         session.commit()
#         session.refresh(new_country)
#         return new_country
#
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
