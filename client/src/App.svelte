<script>
  import Login from "./lib/Login.svelte";
  import Signup from "./lib/Signup.svelte";
  import Home from "./lib/Home.svelte";
  import BookPage from "./lib/BookPage.svelte";

  let basepath = "/";
  const path = window.location.href;
  const segments = path.split("/");
</script>

<!-- <Router {basepath}>
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
</Router> -->

<main>
  {#if segments.length == 4 && segments[segments.length - 1] == "login"}
    <Login></Login>
  {:else if segments.length == 4 && segments[segments.length - 1] == "signup"}
    <Signup></Signup>
  {:else if segments.length == 3 || segments[segments.length - 1] == "home"}
    <Home></Home>
  {:else if segments.length == 5 || (segments[segments.length - 2] == "book" && segments[segments.length - 1])}
    <BookPage bookID={segments[segments.length - 1]}></BookPage>
  {:else}
    <h1>404 - Page Not Found</h1>
    <a href="/home">Go To Home Page</a>
  {/if}
</main>
