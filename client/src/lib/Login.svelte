<script lang="ts">
  import axios, { AxiosError, type AxiosResponse } from "axios";

  let name: string = '';
  let pwd: string = '';
  let res_msg: string = "";

  // Se l'utente è già loggato, reindirizzalo alla home
  if (localStorage.getItem('userID')) {
    window.location.href = 'http://localhost:3000/home';
  }

  // Gestore del form di login
  const handleSubmit = async (e: Event) => {
    e.preventDefault();  // Prevenzione del comportamento predefinito

    try {
      const response: AxiosResponse = await axios.post("http://localhost:8080/login", {
        data: { name, pwd },
      });

      if (response.status === 200) {
        localStorage.setItem("userID", response.data.id);
        window.location.href = "http://localhost:3000/home";
      }
    } catch (error) {
      // Verifica se c'è una risposta di errore e controlla il codice
      if (axios.isAxiosError(error) && error.response) {
        if (error.response.status === 401) {
          res_msg = "Invalid credentials!";
        } else if (error.response.status === 404) {
          res_msg = "User not found!";
        } else {
          res_msg = "Something went wrong. Please try again.";
        }
      }
    }
  };
</script>

<main>
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
</main>
