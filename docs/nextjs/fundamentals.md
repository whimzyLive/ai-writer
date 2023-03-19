# Next.JS Fundamentals

## Introduction

Next.js is a framework built on top of React that provides a set of tools and conventions to simplify the development of enterprise applications. It allows developers to build high-performance web applications with server-rendered React views and automatic code splitting out of the box.

## Key Points

### Page

A page is a React component that is automatically routed based on the file system. Next.js expects pages to be located in the `pages` directory and named according to their file name. For example, if we create a file named `about.js` inside the `pages` directory, Next.js will automatically create a route to `/about`.

```jsx
// pages/about.js

function About() {
  return <h1>About us</h1>
}

export default About
```

### Link

Link is a Next.js component that provides client-side navigation with server-side rendering. It automatically preloads the linked page's content in the background, so that when the user clicks on the link, the new page is loaded instantly.

```jsx
// pages/index.js

import Link from 'next/link'

function Home() {
  return (
    <div>
      <h1>Welcome to my website</h1>
      <Link href="/about">
        <a>About us</a>
      </Link>
    </div>
  )
}

export default Home
```

### Layout

Next.js provides a way to define a layout component that can be shared across pages. By convention, a layout component should be placed in the `components` directory and named `Layout`. Pages can then include the layout component and pass their own content as children.

```jsx
// components/Layout.js

function Layout({ children }) {
  return (
    <div>
      <header>My website</header>
      <main>{children}</main>
      <footer>© 2021 My website</footer>
    </div>
  )
}

export default Layout
```

```jsx
// pages/index.js

import Layout from '../components/Layout'

function Home() {
  return (
    <Layout>
      <h1>Welcome to my website</h1>
      <p>This is the home page</p>
    </Layout>
  )
}

export default Home
```

### Fonts

Next.js automatically hosts and serves web fonts from Google Fonts or the local file system. To use a Google Font, simply import it from `@next/font/google` and add it to the `head` of the page.

```jsx
// pages/index.js

import Head from 'next/head'
import { Inter } from '@next/font/google'

function Home() {
  return (
    <>
      <Head>
        <title>My website</title>
        <Inter />
      </Head>
      <h1>Welcome to my website</h1>
      <p>This is the home page</p>
    </>
  )
}

export default Home
```

### Style

Next.js provides a way to scope styles to a single page or component. Styles can be defined using CSS modules or CSS-in-JS libraries like styled-components.

```jsx
// pages/index.module.css

.title {
  color: red;
}

// pages/index.js

import styles from './index.module.css'

function Home() {
  return (
    <div>
      <h1 className={styles.title}>Welcome to my website</h1>
      <p>This is the home page</p>
    </div>
  )
}

export default Home
```

### Global Style

To apply global styles to all pages, create a file named `_app.js` in the `pages` directory and import the global styles.

```jsx
// pages/_app.js

import '../styles/global.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

### Image

Next.js provides an optimized image component that automatically resizes and optimizes images based on the device size and resolution. Images can be loaded from the local file system or from an external URL.

```jsx
// pages/index.js

import Image from 'next/image'

function Home() {
  return (
    <div>
      <Image src="/my-image.png" width={500} height={500} alt="My image" />
    </div>
  )
}

export default Home
```

### Static Data Fetching

Next.js provides a way to generate static HTML files for pages that do not require server-side rendering. This is useful for pages that do not need to be updated frequently or that have a lot of traffic.

```jsx
// pages/about.js

function About({ data }) {
  return (
    <div>
      <h1>About us</h1>
      <p>{data}</p>
    </div>
  )
}

export async function getStaticProps() {
  const res = await fetch('https://api.example.com/data')
  const data = await res.text()

  return {
    props: {
      data
    },
    revalidate: 1 // regenerate the page every second
  }
}

export default About
```

### Dynamic Data Fetching

Next.js provides a way to fetch data from external APIs on the client-side. To prevent the browser from caching the data, we can use the `cache: 'no-store'` option on the `fetch` API.

```jsx
// pages/products.js

import { useState } from 'react'

function Products({ products }) {
  const [selectedProduct, setSelectedProduct] = useState(null)

  return (
    <div>
      <h1>Products</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <button onClick={() => setSelectedProduct(product)}>
              {product.name}
            </button>
          </li>
        ))}
      </ul>
      {selectedProduct && (
        <div>
          <h2>{selectedProduct.name}</h2>
          <p>{selectedProduct.description}</p>
        </div>
      )}
    </div>
  )
}

export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/products', { cache: 'no-store' })
  const products = await res.json()

  return {
    props: {
      products
    }
  }
}

export default Products
```

## Conclusion

Next.js is a powerful framework that provides a set of tools and conventions to simplify the development of enterprise applications with React. With Next.js, developers can build high-performance web applications with server-rendered views, automatic code splitting, and advanced data fetching capabilities. By following these fundamentals, developers can build scalable and maintainable applications with ease.

## Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Next.js GitHub Repository](https://github.com/vercel/next.js)