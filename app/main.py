from flask import  Flask
from graphene import Schema
from flask_graphql import GraphQLView

from app.db.database import init_db
from app.gql.mutation import Mutation
from app.gql.query import Query

app = Flask(__name__)

schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    init_db()
    app.run(port=5009)