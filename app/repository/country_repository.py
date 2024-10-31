from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models import Country


def find_country_by_id(country_id: int) -> Maybe[Country]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Country).filter(Country.country_id == country_id).first())
