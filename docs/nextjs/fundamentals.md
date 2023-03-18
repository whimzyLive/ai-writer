# Examples of NextJS Fundamentals

If you're new to NextJS, it might seem intimidating at first, but it's a powerful framework that simplifies your development and helps you build enterprise applications with ease. Here are some of the key fundamentals you need to know:

## Pages

Pages are the basic routing units in NextJS. You can think of them as individual routes in your application, and they are defined as files in the `pages` directory. The `page.js` module exports a `default` component that gets rendered for the given route. Here's an example:

```javascript
// pages/index.js
import React from "react";

const HomePage = () => {
  return <h1>Welcome to my website</h1>;
};

export default HomePage;
```

## Link

The `Link` component is used to create client-side navigation between pages in your NextJS application. It automatically prefetches content and provides client-side navigation with server-side routing. Here's an example:

```javascript
// pages/about.js
import React from "react";
import Link from "next/link";

const AboutPage = () => {
  return (
    <div>
      <h1>About Us</h1>
      <Link href="/">
        <a>Go back to home</a>
      </Link>
    </div>
  );
};

export default AboutPage;
```

## Layout

The `Layout` component is used to create page and folder-based layouts that can be shared across multiple pages in your application. You define the layout in a `layout.js` file, and then you can wrap your pages with it to apply the layout. Here's an example:

```javascript
// layouts/default.js
import React from "react";

const DefaultLayout = ({ children }) => {
  return (
    <div>
      <header>Header</header>
      {children}
      <footer>Footer</footer>
    </div>
  );
};

export default DefaultLayout;
```

```javascript
// pages/index.js
import React from "react";
import DefaultLayout from "../layouts/default";

const HomePage = () => {
  return (
    <DefaultLayout>
      <h1>Welcome to my website</h1>
    </DefaultLayout>
  );
};

export default HomePage;
```

## Fonts

NextJS can automatically host and serve your fonts. You can load fonts from `@next/font/{google|local}` using the `@font-face` rule. Here's an example:

```css
@font-face {
  font-family: "Roboto";
  src: url("@next/font/google/roboto/Roboto-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
}
```

## Styles

The `styled-jsx` library is used to create scoped styles for individual pages in your NextJS application. Here's an example:

```javascript
// pages/about.js
import React from "react";

const AboutPage = () => {
  return (
    <div>
      <h1>About Us</h1>
      <style jsx>{`
        h1 {
          color: blue;
        }
      `}</style>
    </div>
  );
};

export default AboutPage;
```

## Global Style

You can also create global styles that apply to all pages in your NextJS application. To do this, you need to import the global style file in your global layout file. Here's an example:

```javascript
// layouts/default.js
import React from "react";
import "../styles/global.css";

const DefaultLayout = ({ children }) => {
  return (
    <div>
      <header>Header</header>
      {children}
      <footer>Footer</footer>
    </div>
  );
};

export default DefaultLayout;
```

## Image

NextJS comes with built-in size optimization and visual stability for images. You can use the `next/image` component to display images in your application. Here's an example:

```javascript
import Image from "next/image";

const MyImage = () => {
  return (
    <div>
      <h1>My Image</h1>
      <Image src="/my-image.png" alt="My Image" width={500} height={500} />
    </div>
  );
};

export default MyImage;
```

## Static Data Fetching

NextJS supports static site generation, which means you can fetch and render data at build time. By default, the `fetch` API in NextJS caches the response. Here's an example:

```javascript
export async function getStaticProps() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = await res.json();

  return {
    props: {
      posts,
    },
  };
}
```

## Dynamic Data Fetching

You can also fetch data dynamically in NextJS using the `getServerSideProps` function. Here's an example:

```javascript
export async function getServerSideProps() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts", {
    cache: "no-store",
  });
  const posts = await res.json();

  return {
    props: {
      posts,
    },
  };
}
```

These are just some of the key fundamentals of NextJS that you need to know to get started with building enterprise applications. With these basics down, you can start building powerful, scalable applications with ease.