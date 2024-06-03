<script lang="ts">
  import axios, { AxiosError, type AxiosResponse } from "axios";

  let name: string, pwd: string;
  let res_msg = "";

  if (localStorage.getItem('userID')) window.location.href = 'http://localhost:3000/home'

  const handleSubmit = (e: Event) => {
    axios
      .post("http://localhost:8080/login", {
        data: { name: name, pwd: pwd },
      })
      .then((response: AxiosResponse) => {
        if (response.status == 200) {
          localStorage.setItem("userID", response.data.id);
          window.location.href = "http://localhost:3000/home";
        }
      })
      .catch((error: AxiosError) => {
        if (error?.response.status == 301) res_msg = "User Not Found";
      });

    e.preventDefault();
  };
</script>

<signup>
  <h1>Login</h1>
  <br />
  <form on:submit={handleSubmit}>
    <input
      type="text"
      class="form-input"
      placeholder="my name or email..."
      bind:value={name}
      maxlength="40"
      required
    />
    <br /> <br />
    <input
      type="password"
      class="form-input"
      placeholder="my secret word..."
      bind:value={pwd}
      maxlength="40"
      required
    />
    <br /> <br />
    <input type="submit" class="main-btn" value="Go" />
  </form>
  <p class="error-msg">{res_msg}</p>
  <a href="/signup">I Don't Have an account</a>
</signup>
