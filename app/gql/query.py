from graphene import ObjectType, List, Field, Int, String, Date


from app.gql.types.mission_type import MissionType
from app.repository.city_repository import find_cities_by_country_id
from app.repository.mission_repository import find_mission_by_id, find_missions_by_date_range, \
    find_missions_by_target_ids
from app.repository.target_repository import find_targets_by_cities_ids, find_targets_by_target_industry, \
    find_targets_by_target_type_id


class Query(ObjectType):
    mission_by_mission_id = Field(MissionType, mission_id=Int())
    missions_in_date_range = List(MissionType, start_date=Date(), end_date=Date())
    missions_by_country_id = List(MissionType, country_id=Int())
    mission_by_target_industry = List(MissionType, target_industry=String())
    mission_by_target_type_id = List(MissionType, target_type_id=Int())

    @staticmethod
    def resolve_mission_by_mission_id(root, info, mission_id):
        return find_mission_by_id(mission_id).value_or(None)

    @staticmethod
    def resolve_missions_in_date_range(root, info, start_date, end_date):
        return find_missions_by_date_range(start_date, end_date)

    @staticmethod
    def resolve_missions_by_country_id(root, info, country_id):
        return find_missions_by_target_ids(
            list(t.target_id for t in find_targets_by_cities_ids(
                list(c.city_id for c in find_cities_by_country_id(country_id))
            ))
        )

    @staticmethod
    def resolve_mission_by_target_industry(root, info, target_industry):
        return find_missions_by_target_ids(
            list(t.target_id for t in find_targets_by_target_industry(target_industry))
        )

    @staticmethod
    def resolve_mission_by_target_type_id(root, info, target_type_id):
        return find_missions_by_target_ids(
            list(t.target_id for t in find_targets_by_target_type_id(target_type_id))
        )


