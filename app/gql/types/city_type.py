from graphene import ObjectType, Int, String, List, Field


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = String()
    longitude = String()

    country = Field('app.gql.types.country_type.CountryType')
    targets = List('app.gql.types.target_type.TargetType')

    # @staticmethod
    # def resolve_country(root, info):
    #     return find_country_by_id(root.country_id)

    # @staticmethod
    # def resolve_targets(root, info):
    #     return find_targets_by_city_id(root.city_id)