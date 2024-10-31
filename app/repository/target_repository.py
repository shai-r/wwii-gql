from typing import List
from sqlalchemy import desc

from app.db.database import session_maker
from app.db.models import Target, City


def find_targets_by_city_id(city_id: int) -> List[Target]:
    with session_maker() as session:
        return session.query(Target).filter(Target.city_id == city_id)

def find_targets_by_cities(cities: List[City]) -> List[Target]:
    cities_ids = {c.city_id for c in cities}
    with session_maker() as session:
        return session.query(Target).filter(Target.city_id.in_(cities_ids))

def find_targets_by_target_industry(target_industry: str) -> List[Target]:
    with session_maker() as session:
        return session.query(Target).filter(Target.target_industry == target_industry)

def find_targets_by_target_type_id(target_type_id: int) -> List[Target]:
    with session_maker() as session:
        return session.query(Target).filter(Target.target_type_id == target_type_id).all()

def find_max_target_id():
    with session_maker() as session:
        return session.query(Target).order_by(desc(Target.target_id)).first().target_id + 1

def create_new_target(new_target: Target):
    with session_maker() as session:
        new_target.target_id = find_max_target_id()
        session.add(new_target)
        session.commit()
        session.refresh(new_target)
        return new_target
