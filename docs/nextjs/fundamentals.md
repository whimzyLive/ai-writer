# Next.JS: Fundamentals

## Introduction

Next.js is a framework for building enterprise-level applications with React. It provides a set of tools and pre-configured functionalities that simplify the development process and enhance the performance of web applications.

In this article, we will be discussing some of the fundamental aspects of Next.js that are essential to building high-quality applications.

## Key Points

### Page

Pages are the basic routing units of Next.js. They are created using the `page.js` module, which enables automatic code splitting and static optimization. Each page can define its own set of properties and is handled by the server using Next.js' built-in routing mechanism.

To create a new page, simply create a new `.js` or `.tsx` file inside the `pages/` directory of your Next.js project.

```javascript
function HomePage() {
  return <div>Hello, World!</div>;
}

export default HomePage;
```

### Link

Link is a component in Next.js that provides a client-side navigation experience while ensuring server-side routing. It automatically prefetches content for faster page loads.

```javascript
import Link from "next/link";

function Home() {
  return (
    <div>
      <Link href="/about">
        <a>About Page</a>
      </Link>
    </div>
  );
}

export default Home;
```

### Layout

Layouts are a way to share a common set of components across multiple pages in your Next.js application. This is achieved by creating a `layout.js` file that exports a React component. Each page that requires the layout can then use it as a higher-order component.

```javascript
import Layout from "../components/layout";

function HomePage() {
  return <Layout>Hello, World!</Layout>;
}

export default HomePage;
```

### Fonts

Next.js provides a built-in mechanism for hosting and serving fonts through its `@next/font` module. This module supports loading fonts from either Google Fonts or local files.

```javascript
import "../fonts.css"; // global font style

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

### Style

Next.js provides a scoped styling mechanism that ensures that the styles defined in a particular component do not interfere with the styles of other components on the page.

```javascript
function MyComponent() {
  return (
    <div>
      <h1 className="text-blue-500">Hello, World!</h1>
      <style jsx>{`
        .text-blue-500 {
          color: blue;
        }
      `}</style>
    </div>
  );
}

export default MyComponent;
```

### Global Style

To add global styles to your Next.js application, you need to import them into the global layout file. This can be done by creating a `global.css` file in the `public/` directory of your Next.js project and importing it in the `pages/_app.js` file.

```javascript
import "../public/global.css"; // global styles

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

### Image

Next.js provides built-in image optimization capabilities that ensure images are optimized for size and visual stability. To use images in your Next.js application, you can import them directly into your JSX code.

```javascript
import Image from "next/image";

function MyImageComponent() {
  return (
    <div>
      <Image
        src="/images/myimage.jpg"
        alt="My Image"
        width={500}
        height={500}
      />
    </div>
  );
}

export default MyImageComponent;
```

### Static Data Fetching

Next.js supports static site generation through its `getStaticProps` function. This function is used to fetch data at build time and is ideal for pages that have static data.

```javascript
export async function getStaticProps() {
  const data = await fetch("https://myapi.com/data");
  const jsonData = await data.json();

  return {
    props: {
      data: jsonData,
    },
  };
}

function MyPage({ data }) {
  return <div>{data}</div>;
}

export default MyPage;
```

### Dynamic Data Fetching

Next.js supports dynamic data fetching through its `getServerSideProps` function. This function is used to fetch data at runtime and is ideal for pages that require dynamic data.

```javascript
export async function getServerSideProps(context) {
  const data = await fetch("https://myapi.com/data");
  const jsonData = await data.json();

  return {
    props: {
      data: jsonData,
    },
  };
}

function MyPage({ data }) {
  return <div>{data}</div>;
}

export default MyPage;
```

## Conclusion

Next.js is a powerful framework for building enterprise-level applications with React. By mastering the fundamentals discussed in this article, you will be able to build scalable, high-performance web applications with ease.