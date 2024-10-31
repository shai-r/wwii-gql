from graphene import ObjectType, Int, String, List

from app.repository.target_repository import find_targets_by_target_type_id


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_targets(root, info):
        return find_targets_by_target_type_id(root.target_type_id)
