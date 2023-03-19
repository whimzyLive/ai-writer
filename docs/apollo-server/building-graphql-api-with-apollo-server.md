# Building a GraphQL API with Apollo Server

## Introduction

GraphQL has taken the world of APIs by storm. One of the most popular implementations of GraphQL on Node.js is Apollo Server. In this blog, we'll go over the basics of building a GraphQL API with Apollo Server.

## What is Apollo in Node.js

Apollo Server is a library that helps you build a GraphQL API on Node.js. It's built on top of the graphql-js library, which is a popular implementation of GraphQL on JavaScript.

## Working with Apollo

### Setting up Apollo

To get started with Apollo Server, first, install the necessary packages. Run the following command to install the dependencies:

```bash
npm install apollo-server graphql
```

Once you have the packages installed, you can create an Apollo Server by importing the `ApolloServer` class from the `apollo-server` package.

```javascript
const { ApolloServer } = require('apollo-server');
```

### Defining a Schema

The next step is to define a schema for your API. A schema is essentially a contract between the server and the client that specifies what types of data the server can provide. You can define a schema using the `typeDefs` and `resolvers` properties of the `ApolloServer` class.

```javascript
const typeDefs = `
  type Query {
    hello: String
  }
`;

const resolvers = {
  Query: {
    hello: () => 'Hello World!'
  }
};

const server = new ApolloServer({ typeDefs, resolvers });
```

In this example, we're defining a simple schema that exposes a single query called `hello` that returns the string `Hello World!`.

### Running the Server

Once you have defined your schema, you can start the server by calling the `listen` method on the `ApolloServer` instance.

```javascript
server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
```

This will start the Apollo Server and log the URL where it's running to the console.

### Using GraphQL Studio

Apollo Server comes with a built-in GraphQL IDE called GraphQL Studio. You can access it by visiting the URL where your Apollo Server is running and appending `/graphql` to the end of it.

![GraphQL Studio](https://i.imgur.com/3wVhVIH.png)

### Introspection

One of the powerful features of GraphQL is introspection. This allows you to query the API schema at runtime to see what queries, types, fields, and directives it supports. To enable introspection, set the `introspection` property to `true` when creating your `ApolloServer` instance.

```javascript
const server = new ApolloServer({ typeDefs, resolvers, introspection: true });
```

## Conclusion

Apollo Server makes it easy to build a GraphQL API on Node.js. With built-in GraphQL Studio and introspection support, it's a great choice for building APIs of any size.