# Spring 8일차 - Full Stack(React & Spring)

---



### Why Full-Stack Architecture?

- Full Stack Architectures are **complex** to build
  - You need to understand **different languages**
  - You need to understand a **variety of frameworks**
  - You need to use a **variety of tools**
- **Why Full-Stack?**
  - Because they give you **flexibility** and allow **reuse of REST API**
    - **Option** : Create a Mobile App talking to REST API
    - **Option** : Create an IOT App talking to REST API



### What's happening in the background with React?

- We updated the state => React updated the view
  - **How can you update an HTML element?**
    - A HTML page is represented by DOM (Document Object Model)
    - Each element in a HTML page is a node in the DOM
    - You need to update the DOM to update the element
    - HOWEVER, writing code to update the DOM can be complex and slow!
  - **React** takes a **different approach** :
    - **Virtual DOM** : "**virtual**" representation of a UI (kept in memory)
      - React code updates Virtual DOM
    - React **identifies changes** and **synchronized them** to HTML page
      1. React creates Virtual DOM v1 on load of page
      2. You perform an action
      3. React creates Virtual DOM v2 as a result of your action
      4. React performs a diff between v1 and v2
      5. React synchronizes chages (updates HTML page)
- **Summary** : We are NOT updating the DOM directly!
  - React identifies changes and **efficiently** updates the DOM



### React Developer Tools - Chrome Extension

- Chrome Developer Tools extension for React
- **Goal** : Inspect React Component Hierarchies
- Components tab shows :
  - Root React components
  - Sub components that were rendered
- For each component, you can see and edit
  - props
  - state
- **Useful for** :
  - Understanding and Learning React
  - Debugging problems



