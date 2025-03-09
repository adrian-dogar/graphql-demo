from typing import List, Optional
from app.resolvers import (
    resolve_authors, resolve_books, resolve_publishers, resolve_reviews,
    create_author, create_book, create_publisher, add_review
)

import strawberry
from app.models import *

# Query Type (for fetching data)
@strawberry.type
class Query:
    authors: List[Author] = strawberry.field(resolver=resolve_authors)
    books: List[Book] = strawberry.field(resolver=resolve_books)
    publishers: List[Publisher] = strawberry.field(resolver=resolve_publishers)
    reviews: List[Review] = strawberry.field(resolver=resolve_reviews)


# Mutation Type (for creating/updating data)
@strawberry.type
class Mutation:
    create_author: Author = strawberry.field(resolver=create_author)
    create_book: Book = strawberry.field(resolver=create_book)
    create_publisher: Publisher = strawberry.field(resolver=create_publisher)
    add_review: Review = strawberry.field(resolver=add_review)


# Combine Query and Mutation into the Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)