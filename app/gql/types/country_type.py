from graphene import ObjectType, Int, String, List

from app.repository.city_repository import find_cities_by_country_id


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()


    cities = List('app.gql.types.city_type.CityType')

    @staticmethod
    def resolve_cities(root, info):
        return find_cities_by_country_id(root.country_id)
