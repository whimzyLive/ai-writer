# GraphQL Big-Picture: A Beginner's Guide

## Introduction

GraphQL is a powerful API query language and runtime that was developed by Facebook in 2012. It is a specification that is language agnostic and provides a more efficient, powerful and flexible alternative to RESTful APIs. In this article, we will take a look at the key points of GraphQL and its core concepts.

## What is GraphQL?

GraphQL is a query language and runtime that moves the focus of development to client applications. With GraphQL, the client defines the structure of the data that it needs, and the server returns exactly that. This helps to eliminate the under-fetching, over-fetching, and unnecessary network round trips that are common with traditional RESTful APIs.

GraphQL doesn't rely on the HTTP spec for caching and depends on development frameworks to perform the heavy lifting. This makes GraphQL more flexible and efficient between client and server applications.

## GraphQL Core Concepts

### Built-in Scalar Types

GraphQL has built-in scalar types, including `Int`, `Float`, `String`, `Boolean`, `ID`, and `Enums`.

### Queries

Each schema contains at minimum a `Query` type. Queries are used to fetch data from the server. With GraphQL, all fields in a query run in parallel, and only the fields requested by the client are returned.

### Queries Fields

Fields are used to specify the data that the client wants to retrieve from the server.

```graphql
query {
  user {
    firstName
    lastName
    age
  }
}
```

### Queries Arguments

Arguments are used to pass data to the server. Each field and nested object can get its own set of arguments.

```graphql
query {
  user(id: "123") {
    firstName
    lastName
    age
  }
}
```

### Queries Aliases

Aliases are used to rename the result of a field with a given alias.

```graphql
query {
  firstName: user(id: "123") {
    firstName
  }
  lastName: user(id: "123") {
    lastName
  }
}
```

### Queries Fragments

Fragments are reusable units in GraphQL, like functions in other programming languages.

```graphql
fragment UserInfo on User {
  firstName
  lastName
  age
}

query {
  user(id: "123") {
    ...UserInfo
  }
}
```

### Queries Variables

Variables are used to make GraphQL queries dynamic.

```graphql
query($id: ID!) {
  user(id: $id) {
    firstName
    lastName
    age
  }
}
```

### Mutations

Mutations are used to create, update, and delete data in the server. Mutations always run in sequence.

```graphql
mutation {
  createUser(
    input: {
      firstName: "John"
      lastName: "Doe"
      age: 25
    }
  ) {
    id
    firstName
    lastName
    age
  }
}
```

## Why GraphQL?

GraphQL provides a way to declaratively fetch data, allowing for a more efficient and powerful way to retrieve data from the server. With GraphQL, the schema contract between the frontend and the backend is stronger, providing a more solid foundation for development. GraphQL provides a superior developer experience, and it is a cost-effective solution since it leads to quicker development and self-documentation.

## GraphQL Tools

GraphQL Voyager is an interactive tool that displays relations between graphs. GraphQL Faker generates fake data for testing, and GraphQL Visual Editor converts visual blocks into code.

## Conclusion

GraphQL is a powerful query language and runtime that is more efficient, powerful and flexible than traditional RESTful APIs. Its built-in scalar types, queries, mutations, and other features provide a superior developer experience, making it an ideal choice for modern web applications.