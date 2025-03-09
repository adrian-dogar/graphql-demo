from typing import List, Optional
from app.db import authors_data, books_data, publishers_data, reviews_data, Author, Book, Publisher, Review


# Query Resolvers
def resolve_authors(order_by: Optional[str] = None) -> List[Author]:
    authors = authors_data
    if order_by == "name":
        authors = sorted(authors, key=lambda x: x.name)
    return [Author(id=a.id, name=a.name, birthdate=a.birthdate, books=a.books) for a in authors]


def resolve_books(author_id: Optional[int] = None, order_by: Optional[str] = None) -> List[Book]:
    books = books_data
    if author_id is not None:
        books = [book for book in books if book.author.id == author_id]
    if order_by == "title":
        books = sorted(books, key=lambda x: x.title)
    return [
        Book(
            id=b.id,
            title=b.title,
            publication_year=b.publication_year,
            author=b.author,
            reviews=b.reviews,
        )
        for b in books
    ]


def resolve_publishers() -> List[Publisher]:
    return [
        Publisher(
            id=p.id,
            name=p.name,
            country=p.country,
            published_books=p.published_books,
        )
        for p in publishers_data
    ]


def resolve_reviews(book_id: Optional[int] = None) -> List[Review]:
    reviews = reviews_data
    if book_id is not None:
        reviews = [review for review in reviews if review.book.id == book_id]
    return [
        Review(
            id=r.id,
            reviewer_name=r.reviewer_name,
            content=r.content,
            book=r.book,
        )
        for r in reviews
    ]


# Mutation Resolvers
def create_author(name: str, birthdate: str) -> Author:
    new_author = Author(id=len(authors_data) + 1, name=name, birthdate=birthdate, books=[])
    authors_data.append(new_author)
    return new_author


def create_book(title: str, publication_year: int, author_id: int) -> Book:
    author = next((a for a in authors_data if a.id == author_id), None)
    if author is None:
        raise ValueError("Author not found")
    new_book = Book(id=len(books_data) + 1, title=title, publication_year=publication_year, author=author, reviews=[])
    books_data.append(new_book)
    author.books.append(new_book)
    return new_book


def create_publisher(name: str, country: str) -> Publisher:
    new_publisher = Publisher(id=len(publishers_data) + 1, name=name, country=country, published_books=[])
    publishers_data.append(new_publisher)
    return new_publisher


def add_review(book_id: int, reviewer_name: str, content: str) -> Review:
    book = next((b for b in books_data if b.id == book_id), None)
    if book is None:
        raise ValueError("Book not found")
    new_review = Review(id=len(reviews_data) + 1, reviewer_name=reviewer_name, content=content, book=book)
    reviews_data.append(new_review)
    book.reviews.append(new_review)
    return new_review
