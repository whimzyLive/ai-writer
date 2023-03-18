# Next.JS Fundamentals

## Introduction
In recent years, JavaScript and React have become key technologies for building modern web applications. Next.js is a framework that takes these technologies to the next level by enabling you to build enterprise-level applications with ease. In this post, we will explore the core concepts of Next.js.

## Key Points

### Page
A page is a basic building block of a Next.js application. It's a React component that represents a URL route. Pages are automatically rendered on the server and cached for future use. This allows for fast and reliable rendering, with the ability to handle many concurrent requests.

```jsx
// pages/index.js

function HomePage() {
  return <div>Welcome to Next.js!</div>;
}

export default HomePage;
```

### Link
The `Link` component in Next.js is used for client-side navigation with server-side routing. It prefetches the content of the destination page in the background, so it can be displayed immediately when the user clicks the link.

```jsx
// pages/index.js

import Link from 'next/link';

function HomePage() {
  return (
    <div>
      <Link href="/about">
        <a>About</a>
      </Link>
      <div>Welcome to Next.js!</div>
    </div>
  );
}

export default HomePage;
```

### Layout
The `Layout` component is used for sharing page layouts across multiple pages or folders. It's a great way to keep your code organized and consistent. A layout is just a React component that wraps your page component.

```jsx
// components/Layout.js

function Layout({ children }) {
  return (
    <div>
      <header>Header</header>
      <main>{children}</main>
      <footer>Footer</footer>
    </div>
  );
}

export default Layout;
```

```jsx
// pages/index.js

import Layout from '../components/Layout';

function HomePage() {
  return (
    <Layout>
      <div>Welcome to Next.js!</div>
    </Layout>
  );
}

export default HomePage;
```

### Fonts
Next.js automatically hosts and serves fonts using the `@next/font` package. You can load Google Fonts or local fonts by importing them from the `@next/font/google` or `@next/font/local` packages, respectively.

```jsx
// components/Layout.js

import Head from 'next/head';
import { GoogleFont } from '@next/font/google';

function Layout({ children }) {
  return (
    <div>
      <Head>
        <GoogleFont href="https://fonts.googleapis.com/css?family=Roboto" />
      </Head>
      <header>Header</header>
      <main>{children}</main>
      <footer>Footer</footer>
    </div>
  );
}

export default Layout;
```

### Style
The `styled-jsx` package is used for styling components in Next.js. It provides a scoped style solution that only applies to the component it's used in. You can use it by adding a `style` tag with a `jsx` attribute to your component.

```jsx
// components/Header.js

export default function Header() {
  return (
    <header>
      <style jsx>{`
        header {
          background-color: #333;
          color: #fff;
          padding: 20px;
        }
      `}</style>
      <h1>My Next.js App</h1>
    </header>
  );
}
```

### Global Style
Global styles can be added to your Next.js application by importing them into your global layout file.

```css
/* styles/globals.css */

body {
  font-family: 'Roboto', sans-serif;
}
```

```jsx
// components/Layout.js

import '../styles/globals.css';

function Layout({ children }) {
  return (
    <div>
      <header>Header</header>
      <main>{children}</main>
      <footer>Footer</footer>
    </div>
  );
}

export default Layout;
```

### Image
The `next/image` component is used for optimizing image performance in Next.js. It automatically optimizes images for size and visual stability by using the `blur-up` technique. It also supports lazy loading and responsive images.

```jsx
// components/Avatar.js

import Image from 'next/image';

export default function Avatar() {
  return (
    <div>
      <Image
        src="/avatar.png"
        alt="Avatar"
        width={64}
        height={64}
      />
    </div>
  );
}
```

### Static Data Fetching
Next.js supports static site generation, where pages are pre-rendered at build time. This allows for faster page loads and better SEO performance. You can use the built-in `getStaticProps` function to fetch data at build time and pass it as props to your page component.

```jsx
// pages/index.js

export default function HomePage({ posts }) {
  return (
    <div>
      <h1>Latest Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <Link href={`/posts/${post.id}`}>
              <a>{post.title}</a>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export async function getStaticProps() {
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();

  return {
    props: { posts },
  };
}
```

### Dynamic Data Fetching
Next.js also supports dynamic data fetching, where pages are rendered on the server with data that can change over time. You can use the built-in `getServerSideProps` function to fetch data at runtime and pass it as props to your page component.

```jsx
// pages/posts/[id].js

export default function PostPage({ post }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}

export async function getServerSideProps({ params }) {
  const { id } = params;
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
  const post = await res.json();

  return {
    props: { post },
  };
}
```

## Conclusion
In this post, we explored the fundamentals of Next.js, a powerful framework for building enterprise applications with React. We covered key concepts such as pages, links, layouts, fonts, styling, images, static and dynamic data fetching. Armed with this knowledge, you can now start building high-performance web applications with ease.