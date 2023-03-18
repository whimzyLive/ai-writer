# Next.js Fundamentals

## Introduction

Next.js is a popular framework for building enterprise applications with React. It offers a lot of benefits, such as built-in server-side rendering, automatic code splitting, and optimized performance. In this guide, we'll cover the basics of Next.js and explore its key features.

## Key Points

### Page

The `Page` component is used for basic routing in Next.js. By creating a file named `pages/example.js`, you can create a route for the URL `/example`. Here's an example of a simple page component:

```jsx
function ExamplePage() {
  return <h1>Hello, World!</h1>;
}

export default ExamplePage;
```

### Link

The `Link` component is used to provide client-side navigation with server-side routing. It also automatically prefetches content, making navigation faster for users. Here's an example of how to use the `Link` component:

```jsx
import Link from 'next/link';

function HomePage() {
  return (
    <>
      <h1>Welcome to my site!</h1>
      <Link href="/example">
        <a>Go to Example Page</a>
      </Link>
    </>
  );
}

export default HomePage;
```

### Layout

The `Layout` component is used for page and folder-based layout sharing. You can create a `Layout` component to provide a consistent look and feel across all pages of your application. Here's an example of how to use the `Layout` component:

```jsx
import Layout from '../components/Layout';

function ExamplePage() {
  return (
    <Layout>
      <h1>Hello, World!</h1>
    </Layout>
  );
}

export default ExamplePage;
```

### Fonts

Next.js automatically hosts and serves fonts. You can load fonts from the `@next/font/{google|local}` package. Here's an example of how to load a font from the `@next/font/google` package:

```jsx
import { Global } from '@emotion/react';
import { GoogleFont } from 'next/font/google';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <GoogleFont href="https://fonts.googleapis.com/css2?family=Roboto" />
      <Global
        styles={`
          body {
            font-family: 'Roboto', sans-serif;
          }
        `}
      />
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
```

### Style

The `style` attribute in Next.js scopes styles to the nested page. This helps to prevent CSS collisions between different components. Here's an example of how to use the `style` attribute:

```jsx
function ExamplePage() {
  return (
    <div style={{ backgroundColor: 'blue', color: 'white' }}>
      <h1>Hello, World!</h1>
    </div>
  );
}

export default ExamplePage;
```

### Global Style

Global styles need to be imported into the global layout file. Here's an example of how to import global styles:

```jsx
import { Global } from '@emotion/react';

function Layout({ children }) {
  return (
    <>
      <Global
        styles={`
          body {
            background-color: #f0f0f0;
          }
        `}
      />
      {children}
    </>
  );
}

export default Layout;
```

### Image

Next.js has built-in image optimization features, such as size optimization and visual stability. Here's an example of how to use the `Image` component:

```jsx
import Image from 'next/image';

function ExamplePage() {
  return (
    <>
      <h1>Hello, World!</h1>
      <Image src="/example.png" alt="Example Image" width={300} height={300} />
    </>
  );
}

export default ExamplePage;
```

### Static Data Fetching

Next.js has support for static site generation, which is useful for building static pages. You can use the default `fetch` API in Next.js to fetch data. The response is cached by default. Here's an example of how to fetch data statically:

```jsx
export async function getStaticProps() {
  const data = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await data.json();

  return {
    props: { posts },
  };
}

function ExamplePage({ posts }) {
  return (
    <>
      <h1>Hello, World!</h1>
      {posts.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.body}</p>
        </div>
      ))}
    </>
  );
}

export default ExamplePage;
```

### Dynamic Data Fetching

Next.js also supports dynamic data fetching, which is useful for building dynamic pages. You can use the `cache: "no-store"` option on the `fetch` API to prevent caching. Here's an example of how to fetch data dynamically:

```jsx
export async function getServerSideProps() {
  const data = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await data.json();

  return {
    props: { posts },
  };
}

function ExamplePage({ posts }) {
  return (
    <>
      <h1>Hello, World!</h1>
      {posts.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.body}</p>
        </div>
      ))}
    </>
  );
}

export default ExamplePage;
```

## Conclusion

Next.js is a powerful framework for building enterprise applications with React. Its built-in features, such as server-side rendering, automatic code splitting, and optimized performance, make it a popular choice for developers. By understanding the key points covered in this guide, you'll be able to build robust and scalable applications with Next.js.