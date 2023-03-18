# Building a GraphQL API with Apollo Server

## Introduction

GraphQL is a powerful query language used to communicate with APIs. Apollo Server is a node.js implementation of GraphQL that makes it easy to build a powerful API in a short amount of time. In this post, we’ll explore the basics of building a GraphQL API with Apollo Server.

## What is Apollo

Apollo Server is a community-maintained open-source project that makes it easy to build a GraphQL API. Apollo has become one of the most popular and well-supported libraries for building GraphQL APIs.

## Working with Apollo

To get started with Apollo Server, we need to install it via npm. We can do this by running:

```
npm install apollo-server
```

With Apollo installed, we can begin building our API. Apollo Server comes with a built-in GraphQL studio that we can use to view our API schema and make test queries. We can start the server by creating a file called `index.js` with the following code:

```javascript
const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
  type Query {
    hello: String
  }
`;

const resolvers = {
  Query: {
    hello: () => 'Hello, world!',
  },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
```

In this example, we define a single query called `hello` that returns the string “Hello, world!”. We then create a new `ApolloServer` instance with our type definitions and resolvers, and start the server. We can then navigate to `http://localhost:4000` to see our GraphQL studio.

### Introspection

Introspection is a powerful feature of GraphQL that allows us to query the schema of our API. With introspection, we can see the queries, types, fields, and directives that our API supports.

To use introspection, we can make a special query called `__schema` that returns information about the API schema. We can make this query by running the following code in our GraphQL studio:

```graphql
query {
  __schema {
    types {
      name
    }
  }
}
```

This will return a list of all the types that are defined in our schema.

## Examples

Let’s look at an example of how we can use Apollo Server to build a simple API for a blog. Our API will allow users to retrieve blog posts and create new ones.

```javascript
const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
  type Query {
    posts: [Post!]!
  }

  type Mutation {
    addPost(input: AddPostInput!): Post!
  }

  input AddPostInput {
    title: String!
    content: String!
  }

  type Post {
    id: ID!
    title: String!
    content: String!
  }
`;

let posts = [
  { id: '1', title: 'My first post', content: 'This is my first blog post' },
  { id: '2', title: 'My second post', content: 'This is my second blog post' },
];

const resolvers = {
  Query: {
    posts: () => posts,
  },
  Mutation: {
    addPost: (_, { input }) => {
      const id = String(posts.length + 1);
      const post = { id, ...input };
      posts.push(post);
      return post;
    },
  },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
```

In this example, we define a `Post` type with fields for `id`, `title`, and `content`. We also define a `Query` type with a field for retrieving all blog posts, as well as a `Mutation` type with a field for adding a new post. We then implement these types in our `resolvers`.

## Conclusion

In this post, we’ve explored the basics of building a GraphQL API with Apollo Server. We looked at how to install Apollo, how to use GraphQL studio, and how to use introspection to explore our API schema. We also looked at an example of how to build a simple API for a blog. With Apollo Server, we can build powerful APIs with ease.