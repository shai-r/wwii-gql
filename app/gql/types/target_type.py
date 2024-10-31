from graphene import ObjectType, Int, String, List, Field

from app.repository.mission_repository import find_mission_by_id


# target_id = Column(Integer, primary_key=True, autoincrement=True)
#    mission_id = Column(Integer, ForeignKey('missions.id'))
#    city_id = Column(Integer, ForeignKey('cities.id'))
#    target_type_id = Column(Integer, ForeignKey('target_types.id'))
#    target_priority = Column(Integer)

class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    mission = Field('app.gql.types.mission_type.MissionType')
    city = Field('app.gql.types.city_type.CityType')
    target_type = Field('app.gql.types.target_type_type.TargetTypeType')

    @staticmethod
    def resolve_mission(root, info):
        return find_mission_by_id(root.mission_id)

    # @staticmethod
    # def resolve_city(root, info):
    #     return find_city_by_id(root.city_id)

    # @staticmethod
    # def resolve_target_type(root, info):
    #     return find_target_type_by_id(root.target_type_id)
