<script lang="ts">
  import axios, { AxiosError, type AxiosResponse } from "axios";

  let name: string, pwd: string, email: string;
  let res_msg = "";

  if (localStorage.getItem("userID"))
    window.location.href = "http://localhost:3000/home";

  const handleSubmit = (e: Event) => {
    axios
      .post("http://localhost:8080/signup", {
        data: { name: name, pwd: pwd, email: email },
      })
      .then((response: AxiosResponse) => {
        if (response.status == 201)
          window.location.href = "http://localhost:3000/login";
      })
      .catch((error: AxiosError) => {
        if (error?.response.status == 300)
          res_msg = "User Already Existing, try another username or email!";
      });

    e.preventDefault();
  };
</script>

<signup>
  <h1>Signup</h1>
  <br />
  <form on:submit={handleSubmit}>
    <input
      type="text"
      class="form-input"
      placeholder="my name..."
      bind:value={name}
      maxlength="20"
      required
    />
    <br /> <br />
    <input
      type="email"
      class="form-input"
      placeholder="my email..."
      bind:value={email}
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
  <a href="/login">I Already Have an account</a>
</signup>
