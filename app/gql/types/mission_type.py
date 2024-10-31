from graphene import ObjectType, Int, Date, Float



class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

    # targets = List('app.gql.types.target_type.TargetType')

    # @staticmethod
    # def resolve_targets(root, info):
    #     return find_targets_by_mission_id(root.mission_id)
