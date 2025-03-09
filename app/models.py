import strawberry
from typing import List, Optional

# Define the data types (GraphQL Schema)

@strawberry.type
class Author:
    id: int
    name: str
    birthdate: str
    books: List["Book"]


@strawberry.type
class Book:
    id: int
    title: str
    publication_year: int
    author: Author
    reviews: List["Review"]


@strawberry.type
class Publisher:
    id: int
    name: str
    country: str
    published_books: List[Book]


@strawberry.type
class Review:
    id: int
    reviewer_name: str
    content: str
    book: Book
