# Building a GraphQL API with Apollo Server

## Introduction

GraphQL is a query language and runtime for APIs that was developed by Facebook. It allows clients to request only the data that they need from an API, which can lead to faster and more efficient data fetching. Apollo is a popular open-source implementation of GraphQL for Node.js and is commonly used for building APIs.

In this blog post, we will be discussing the basics of building a GraphQL API with Apollo Server, including what Apollo is and how to work with it.

## What is Apollo

Apollo is a set of libraries and tools that can be used to build GraphQL APIs. It includes Apollo Server, which is a production-ready GraphQL server that can be used with any JavaScript HTTP server framework. Apollo also provides client libraries that make it easy to consume GraphQL APIs from web and mobile apps.

## Working with Apollo

### Setting up Apollo Server

To get started with Apollo Server, we need to install the `apollo-server` npm package. This can be done by running the following command in your terminal:

```
npm install apollo-server
```

Once installed, we can create a new instance of Apollo Server by passing in a configuration object. Here's an example:

```javascript
const { ApolloServer, gql } = require('apollo-server');

// Define our GraphQL schema using the gql tag
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

// Define a resolver for our query
const resolvers = {
  Query: {
    hello: () => 'Hello world!',
  },
};

// Create a new instance of ApolloServer
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server
server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
```

In this example, we're defining a simple GraphQL schema that includes a single query called `hello` that returns a string. We've also defined a resolver for the `hello` query that returns the string `'Hello world!'`. Finally, we create a new instance of ApolloServer and start it listening on a port.

### Using GraphQL Playground

When we start Apollo Server, it automatically launches a GraphQL playground, which is a web-based IDE that can be used to interact with our API. The playground can be accessed by navigating to `http://localhost:4000` in a web browser (assuming we're running our server on port 4000).

Using the playground, we can explore our API and execute queries. For example, we could execute the following query:

```graphql
query {
  hello
}
```

This should return the following response:

```json
{
  "data": {
    "hello": "Hello world!"
  }
}
```

### Introspection

One of the key benefits of using GraphQL is its introspection capabilities. Introspection refers to the ability to query which resources are available in the current API schema. Using introspection, we can see the queries, types, fields and directives that our API supports.

Apollo provides a built-in `introspection` query that can be used to retrieve the current schema of our API. We can execute this query in GraphQL Playground by clicking the "Schema" tab and then clicking the "Introspection" button.

Here's an example of what the `introspection` query response might look like:

```json
{
  "__schema": {
    "queryType": {
      "name": "Query"
    },
    "types": [
      {
        "kind": "OBJECT",
        "name": "Query",
        "fields": [
          {
            "name": "hello",
            "args": [],
            "type": {
              "kind": "SCALAR",
              "name": "String",
              "ofType": null
            },
            "isDeprecated": false,
            "deprecationReason": null
          }
        ]
      },
      {
        "kind": "SCALAR",
        "name": "String",
        "description": "The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text."
      }
    ]
  }
}
```

This response tells us that our API has a single query called `hello`, which returns a string. We can use this information to build more complex queries and to better understand the capabilities of our API.

## Conclusion

In this blog post, we've covered the basics of building a GraphQL API with Apollo Server. We've discussed what Apollo is, how to set up a basic server with Apollo, and how to use GraphQL Playground and introspection to explore our API.

GraphQL and Apollo provide a powerful way to build APIs that are flexible, efficient, and easy to consume. By using these technologies, we can create APIs that meet the needs of our clients and provide a great developer experience.

## Additional Resources

- [Apollo Server Documentation](https://www.apollographql.com/docs/apollo-server/)
- [GraphQL Documentation](https://graphql.org/learn/)
- [GraphQL Playground Documentation](https://github.com/graphql/graphql-playground)