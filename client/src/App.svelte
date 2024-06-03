<script>
  import { Route, Router } from "svelte-routing";
  import Login from "./lib/Login.svelte";
  import Signup from "./lib/Signup.svelte";
  import Home from "./lib/Home.svelte";
  import BookPage from "./lib/BookPage.svelte";

  let basepath = "/";
  const getBookParam = () => {
    const path = window.location.href;
    const segments = path.split("/");
    return segments[segments.length - 1];
  };
</script>

<Router {basepath}>
  <main>
    <Route path="/login" component={Login}></Route>

    <Route path="/signup" component={Signup}></Route>

    <Route path="/" component={Home}></Route>

    <Route path="/home" component={Home}></Route>

    <Route path="/book/:id">
      <BookPage bookID={getBookParam()}></BookPage>
    </Route>

    <Route>
      <h1>404 - Page Not Found</h1>
      <a href="/home">Go To Home Page</a>
    </Route>
  </main>
</Router>
