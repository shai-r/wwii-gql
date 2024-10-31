from typing import List

from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models import City


def find_cities_by_country_id(country_id: int) -> List[City]:
    with session_maker() as session:
        return session.query(City).filter(City.country_id == country_id)

def find_city_by_id(city_id: int) -> Maybe[City]:
    with session_maker() as session:
        return session.query(City).filter(City.city_id == city_id)