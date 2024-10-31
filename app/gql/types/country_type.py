from graphene import ObjectType, Int, String, List



class CountryType(ObjectType):
    country_id = Int()
    country_name = String()


    # cities = List('app.gql.types.city_type.CityType')

    # @staticmethod
    # def resolve_cities(root, info):
    #     return find_cities_by_country(root.country_id)
