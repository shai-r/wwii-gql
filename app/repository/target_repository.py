from typing import List

from app.db.database import session_maker
from app.db.models import Target


def find_targets_by_city_id(city_id: int) -> List[Target]:
    with session_maker() as session:
        return session.query(Target).filter(Target.city_id == city_id)

def find_targets_by_cities_ids(cities_ids: List[int]) -> List[Target]:
    with session_maker() as session:
        return session.query(Target).filter(any(Target.city_id == c for c in cities_ids))

def find_targets_by_target_industry(target_industry: str) -> List[Target]:
    with session_maker() as session:
        return session.query(Target).filter(Target.target_industry == target_industry)