# Next.js Fundamentals: Building Enterprise Applications with React

If you are looking to build an enterprise application with React, Next.js is a framework that you should consider using. It provides a lot of useful features, including routing, layout, automatic font hosting, and data fetching. In this post, we'll discuss the key features of Next.js and their basics.

## Introduction

Next.js is a framework that allows you to build server-rendered React applications with ease. It supports both client-side and server-side rendering and provides a lot of useful features out of the box. Some of the key benefits of using Next.js include automatic code splitting, optimized performance, and easy deployment.

## Key Points

### Page

Next.js uses a file-based routing system. This means that you can create a file in the pages directory and that file will become a route that users can access. For example, if you create a file called `about.js` in the pages directory, you can access that page at `/about`.

### Link

The Link component in Next.js is used for client-side navigation. It automatically prefetches content so that when a user clicks on a link, the next page is loaded instantly. This provides a seamless browsing experience for users. 

```javascript
import Link from 'next/link'

<Link href="/about">
  <a>About Us</a>
</Link>
```

### Layout

Next.js provides a layout system that allows you to share layout components between pages. You can create a `_app.js` file in the pages directory and define your layout there. 

```javascript
function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}

export default MyApp
```

### Fonts

Next.js automatically hosts and serves fonts for you. You can load fonts from `@next/font/{google|local}`. For example, to load the Roboto font from Google, you would use the following code:

```javascript
import "@next/font/google/roboto.css"
```

### Style

Next.js provides a style system that scopes styles to the nested page. This means that styles defined in one page do not affect other pages. 

```javascript
import styles from './about.module.css'

function About() {
  return <div className={styles.container}>About Us</div>
}
```

### Global Style

Global styles need to be imported into the global layout file. For example, to import a global CSS file, you would use the following code:

```javascript
import '../styles/global.css'
```

### Image

Next.js provides a built-in image component that optimizes image sizes and ensures visual stability. 

```javascript
import Image from 'next/image'

function About() {
  return <Image src="/image.jpg" width={500} height={500} alt="image" />
}
```

### Static Data Fetching

Next.js supports static site generation, which means that it can generate HTML pages at build time. This can improve performance and reduce server load. 

```javascript
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/data')
  const jsonData = await data.json()

  return {
    props: {
      data: jsonData
    },
    revalidate: 60 // regenerates the page every 60 seconds
  }
}
```

### Dynamic Data Fetching

Next.js supports dynamic data fetching, which means that it can fetch data at runtime. By default, the fetch API in Next.js caches responses. If you want to disable caching, you can use the `cache: "no-store"` option.

```javascript
export async function getServerSideProps() {
  const data = await fetch('https://api.example.com/data', {
    cache: "no-store"
  })
  const jsonData = await data.json()

  return {
    props: {
      data: jsonData
    }
  }
}
```

## Conclusion

Next.js is a powerful framework for building enterprise applications with React. It provides a lot of useful features out of the box, including routing, layout, automatic font hosting, and data fetching. By using Next.js, you can build high-performance applications with ease.