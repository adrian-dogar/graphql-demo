
queries:

```graphql
query GetAuthorsWithBooks {
  authors {
    name
    birthdate
    books(order_by: "title") {
      title
      publication_year
    }
  }
}
```

```graphql
query GetBooksByAuthor {
  books(author_id: 1) {
    title
    publication_year
  }
}
```

```graphql
query GetAuthorsInOrder {
  authors(order_by: "name") {
    name
    birthdate
  }
}
```

```graphql
query GetReviewsForBook {
  reviews(book_id: 1) {
    reviewer_name
    content
  }
}
```

```graphql
mutation {
  createBook(title: "GraphQL in Action", publicationYear: 2023, authorId: 1) {
    id
    title
    publicationYear
    author {
      id
      name
    }
  }
}
```

pip install uvicorn  strawberry-graphql starlette fastapi
pip freeze > requirements.txt

   docker-compose up --build
