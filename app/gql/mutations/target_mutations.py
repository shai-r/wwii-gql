from graphene import String, Int, Field, Mutation

from app.db.models import Target
from app.gql.types.target_type import TargetType
from app.repository.target_repository import create_new_target


class AddTarget(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        target_industry = String(required=True)
        city_id = Int(required=True)
        target_type_id = Int(required=True)
        target_priority = Int(required=True)

    target = Field(TargetType)

    @staticmethod
    def mutate(root,
               info,
               mission_id,
               target_industry,
               city_id,
               target_type_id,
               target_priority):
        new_target = Target(
            mission_id=mission_id,
            target_industry=target_industry,
            city_id=city_id,
            target_type_id=target_type_id,
            target_priority=target_priority
        )
        return AddTarget(target=create_new_target(new_target))