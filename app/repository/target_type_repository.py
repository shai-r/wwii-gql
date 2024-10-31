from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models import TargetType


def find_target_type_by_id(target_type_id: int) -> Maybe[TargetType]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(TargetType).filter(TargetType.target_type_id == target_type_id).first())
