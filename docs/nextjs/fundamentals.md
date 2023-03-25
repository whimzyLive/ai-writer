# Next.js Fundamentals

## Introduction

Next.js is a popular open-source framework for building enterprise-level applications with React. It provides a set of powerful features and tools that can help you develop modern web applications faster, easier, and more efficiently.

In this post, we will explore some of the basic Next.js fundamentals that are essential for building scalable and robust applications. We will cover several key points such as page, link, layout, fonts, style, image, static data fetching, and dynamic data fetching.

## Key Points

### Page

Next.js uses a file-based routing system, which means that every page in your application corresponds to a file in the pages directory. For example, if you create a file called `about.js` in the `pages` directory, you can access it at `/about`.

```jsx
// Example of a Next.js page component
import React from 'react';

const AboutPage = () => {
  return (
    <div>
      <h1>About Us</h1>
      <p>We are a company that does cool stuff.</p>
    </div>
  );
};

export default AboutPage;
```

### Link

Next.js provides a `Link` component that allows you to navigate between pages without reloading the entire page. It also automatically prefetches the content of the linked page, which makes the navigation experience faster and smoother.

```jsx
// Example of a Next.js Link component
import Link from 'next/link';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to our website!</h1>
      <Link href="/about">
        <a>Learn more about us</a>
      </Link>
    </div>
  );
};

export default HomePage;
```

### Layout

Next.js allows you to define layouts for your application that can be reused across multiple pages. You can create a `layout.js` file in your `pages` directory to define your layout component, and then use it in your pages by wrapping your content inside the layout component.

```jsx
// Example of a Next.js layout component
import React from 'react';

const MainLayout = ({ children }) => {
  return (
    <div>
      <header>Header</header>
      <main>{children}</main>
      <footer>Footer</footer>
    </div>
  );
};

export default MainLayout;
```

### Fonts

Next.js provides a built-in support for hosting and serving fonts. You can load your fonts from the `@next/font/{google|local}` package and use them in your styles.

```css
/* Example of using Next.js fonts */
@font-face {
  font-family: 'Montserrat';
  src: url('@next/font-googleMontserrat-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
```

### Style

Next.js provides scoped styles by default, which means that your styles are automatically isolated to the page or component that they belong to. You can define your styles using CSS-in-JS libraries like styled-components, emotion, or CSS modules.

```jsx
// Example of using styled-components with Next.js
import styled from 'styled-components';

const StyledButton = styled.button`
  background-color: ${props => (props.primary ? 'blue' : 'white')};
  color: ${props => (props.primary ? 'white' : 'blue')};
  font-size: 1.2rem;
  padding: 1rem 2rem;
  border: none;
  border-radius: 0.5rem;
`;

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to our website!</h1>
      <StyledButton primary>Get started</StyledButton>
    </div>
  );
};

export default HomePage;
```

### Global Style

If you need to define global styles that should be applied across all pages, you can import them in your `_app.js` file, which is the root component of your application.

```jsx
// Example of importing global styles in Next.js
import React from 'react';
import App from 'next/app';
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    font-family: 'Montserrat', sans-serif;
  }
`;

class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props;
    return (
      <>
        <GlobalStyle />
        <Component {...pageProps} />
      </>
    );
  }
}

export default MyApp;
```

### Image

Next.js provides built-in image optimization features that can improve the performance and visual stability of your application. It automatically optimizes the size and format of your images based on the device and screen size, and also supports lazy loading and priority loading.

```jsx
// Example of using the Next.js Image component
import Image from 'next/image';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to our website!</h1>
      <Image
        src="/images/hero.jpg"
        alt="Hero image"
        width={1200}
        height={600}
      />
    </div>
  );
};

export default HomePage;
```

### Static Data Fetching

Next.js provides support for static site generation (SSG), which allows you to pre-render your pages at build time and serve them as static HTML files. You can use the `getStaticProps` function to fetch data for your pages at build time.

```jsx
// Example of using getStaticProps with Next.js
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return {
    props: {
      data,
    },
    revalidate: 60, // revalidate every 60 seconds
  };
}

const HomePage = ({ data }) => {
  return (
    <div>
      <h1>Welcome to our website!</h1>
      <p>{data.message}</p>
    </div>
  );
};

export default HomePage;
```

### Dynamic Data Fetching

Next.js also supports dynamic data fetching, which allows you to fetch data for your pages at runtime. You can use the `getServerSideProps` function to fetch data for your pages on the server-side.

```jsx
// Example of using getServerSideProps with Next.js
export async function getServerSideProps(context) {
  const { id } = context.query;
  const res = await fetch(`https://api.example.com/data/${id}`, {
    headers: {
      'Cache-Control': 'no-store', // disable caching
    },
  });
  const data = await res.json();
  return {
    props: {
      data,
    },
  };
}

const PostPage = ({ data }) => {
  return (
    <div>
      <h1>{data.title}</h1>
      <p>{data.content}</p>
    </div>
  );
};

export default PostPage;
```

## Conclusion

In this post, we have covered some of the key Next.js fundamentals that are essential for building modern web applications with React. We have explored several important features such as page, link, layout, fonts, style, image, static data fetching, and dynamic data fetching. By mastering these fundamentals, you will be able to build scalable and robust applications with Next.js.

If you want to learn more about Next.js, be sure to check out the official documentation and other online resources. Happy coding!