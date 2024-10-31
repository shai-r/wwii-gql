from graphene import Mutation, String, Int, Field, Boolean, Float, Date

from app.db.models import Country, Mission
from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import create_new_mission


class AddMission(Mutation):
    class Arguments:
        mission_date = Date(required=True)
        airborne_aircraft = Float(required=True)
        attacking_aircraft = Float(required=True)
        bombing_aircraft = Float(required=True)
        aircraft_returned = Float(required=True)
        aircraft_failed = Float(required=True)
        aircraft_damaged = Float(required=True)
        aircraft_lost = Float(required=True)

    mission = Field(MissionType)

    @staticmethod
    def mutate(root,
               info,
               mission_date,
               airborne_aircraft,
               attacking_aircraft,
               bombing_aircraft,
               aircraft_returned,
               aircraft_failed,
               aircraft_damaged,
               aircraft_lost):
        new_mission = Mission(
            mission_date=mission_date,
            airborne_aircraft=airborne_aircraft,
            attacking_aircraft=attacking_aircraft,
            bombing_aircraft=bombing_aircraft,
            aircraft_returned=aircraft_returned,
            aircraft_failed=aircraft_failed,
            aircraft_damaged=aircraft_damaged,
            aircraft_lost=aircraft_lost
        )
        return AddMission(mission=create_new_mission(new_mission))

# class UpdateCountry(Mutation):
#     class Arguments:
#         country_id = Int(required=True)
#         region = String()
#         capital = String()
#         name = String()
#
#     success = Boolean()
#
#     @staticmethod
#     def mutate(root, info, country_id, region, capital, name):
#         country_to_update = Country(id=country_id, region=region, capital=capital, name=name)
#         return UpdateCountry(success=update_country(country_to_update))
#
#
# class DeleteCountry(Mutation):
#     class Arguments:
#         country_id = Int()
#
#     success = Boolean()
#
#     @staticmethod
#     def mutate(root, info, country_id):
#         return DeleteCountry(success=delete_country(country_id))
#
#
#
#
#
#
#


