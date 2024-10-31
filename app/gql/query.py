from graphene import ObjectType, List, Field, Int, String, Date


from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import find_mission_by_id, find_missions_by_date_range


class Query(ObjectType):
    mission_by_mission_id = Field(MissionType, mission_id=Int())
    missions_in_date_range = List(MissionType, start_date=Date(), end_date=Date())

    @staticmethod
    def resolve_mission_by_mission_id(root, info, mission_id):
        return find_mission_by_id(mission_id).value_or(None)

    @staticmethod
    def resolve_missions_in_date_range(root, info, start_date, end_date):
        return find_missions_by_date_range(start_date, end_date)
