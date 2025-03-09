from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema

app = FastAPI()
graphql_app = GraphQLRouter(schema)

# Add the GraphQL endpoint
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Bookstore API! Access /graphql for GraphQL endpoint."}


# Export the schema to a .graphql file
@app.on_event("startup")
def export_schema():
    with open("schema.graphql", "w") as f:
        f.write(str(schema))
    print("GraphQL schema exported to schema.graphql")
