from typing import List, Optional

class Author:
    def __init__(self, id: int, name: str, birthdate: str, books: Optional[List["Book"]] = None):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.books = books or []


class Book:
    def __init__(self, id: int, title: str, publication_year: int, author: "Author",
                 reviews: Optional[List["Review"]] = None):
        self.id = id
        self.title = title
        self.publication_year = publication_year
        self.author = author
        self.reviews = reviews or []


class Publisher:
    def __init__(self, id: int, name: str, country: str, published_books: Optional[List[Book]] = None):
        self.id = id
        self.name = name
        self.country = country
        self.published_books = published_books or []


class Review:
    def __init__(self, id: int, reviewer_name: str, content: str, book: Book):
        self.id = id
        self.reviewer_name = reviewer_name
        self.content = content
        self.book = book


# Authors
author_1 = Author(id=1, name="J.R.R. Tolkien", birthdate="1892-01-03", books=[])
author_2 = Author(id=2, name="F. Scott Fitzgerald", birthdate="1896-09-24", books=[])

# Books
book_1 = Book(id=1, title="The Hobbit", publication_year=1937, author=author_1, reviews=[])
book_2 = Book(id=2, title="The Lord of the Rings", publication_year=1954, author=author_1, reviews=[])
book_3 = Book(id=3, title="The Great Gatsby", publication_year=1925, author=author_2, reviews=[])

# Add books to authors
author_1.books.extend([book_1, book_2])
author_2.books.append(book_3)

# Publishers
publisher_1 = Publisher(id=1, name="Allen & Unwin", country="United Kingdom", published_books=[book_1, book_2])
publisher_2 = Publisher(id=2, name="Charles Scribner's Sons", country="United States", published_books=[book_3])

# Reviews
review_1 = Review(id=1, book=book_1, reviewer_name="Alice", content="A fantastic adventure tale.")
review_2 = Review(id=2, book=book_3, reviewer_name="Bob", content="A timeless classic.")

# Add reviews to books
book_1.reviews.append(review_1)
book_3.reviews.append(review_2)

# Database-like structure
authors_data = [author_1, author_2]
books_data = [book_1, book_2, book_3]
publishers_data = [publisher_1, publisher_2]
reviews_data = [review_1, review_2]