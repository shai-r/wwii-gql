from graphene import Mutation, Field, Float, Date, Int, Boolean

from app.db.models import Mission
from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import create_new_mission, update_mission, delete_mission


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
               airborne_aircraft=None,
               attacking_aircraft=None,
               bombing_aircraft=None,
               aircraft_returned=None,
               aircraft_failed=None,
               aircraft_damaged=None,
               aircraft_lost=None):
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

class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        mission_date = Date(required=False)
        airborne_aircraft = Float(required=False)
        attacking_aircraft = Float(required=False)
        bombing_aircraft = Float(required=False)
        aircraft_returned = Float(required=False)
        aircraft_failed = Float(required=False)
        aircraft_damaged = Float(required=False)
        aircraft_lost = Float(required=False)

    success = Boolean()

    @staticmethod
    def mutate(
            root,
            info,
            mission_id,
            mission_date=None,
            airborne_aircraft=None,
            attacking_aircraft=None ,
            bombing_aircraft=None,
            aircraft_returned=None,
            aircraft_failed=None,
            aircraft_damaged=None,
            aircraft_lost=None
    ):
        mission_to_update = Mission(
            mission_id=mission_id,
            mission_date=mission_date,
            airborne_aircraft=airborne_aircraft,
            attacking_aircraft=attacking_aircraft,
            bombing_aircraft=bombing_aircraft,
            aircraft_returned=aircraft_returned,
            aircraft_failed=aircraft_failed,
            aircraft_damaged=aircraft_damaged,
            aircraft_lost=aircraft_lost
        )
        return UpdateMission(success=update_mission(mission_to_update))


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    success = Boolean()

    @staticmethod
    def mutate(root, info, mission_id):
        return DeleteMission(success=delete_mission(mission_id))


