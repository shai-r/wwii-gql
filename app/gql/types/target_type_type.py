from graphene import ObjectType, Int, String, List

import app.gql.types.target_type


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    # targets = List(app.gql.types.target_type.TargetType)

    # @staticmethod
    # def resolve_targets(root, info):
    #     return find_targets_by_target_type_id(root.target_type_id)
