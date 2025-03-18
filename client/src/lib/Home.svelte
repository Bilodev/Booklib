<script lang="ts">
  import axios, { type AxiosResponse } from "axios";
  import type { bookBean, Book, BookView, status } from "../Book";
  import BookC from "./BookC.svelte";
  import SearchResultC from "./SearchResultC.svelte";
  import axiosRateLimit from "axios-rate-limit";

  const userID =
    localStorage.getItem("userID") ||
    (location.href = "http://localhost:3000/login");

  let minimalView = localStorage.getItem("view") == "minimal" ? true : false;

  let booksBeans: bookBean[] = [];
  let bookViews: BookView[] = [];
  let foundBooks: Book[] = [];

  let research: string;
  let currentFilter = "status";
  let currentAscendingOrder = false;

  const apiUrl = "https://www.googleapis.com/books/v1/volumes/";

  // Funzione per ottenere la vista dei libri
  const get_books_view = async () => {
    const http = axiosRateLimit(axios.create(), {
      maxRequests: booksBeans.length,
      perMilliseconds: 1000,
    });

    const cleanHtmlTags = (input: string) => input?.replaceAll(/<[^>]*>/g, "");

    // Crea un array di promesse per le chiamate API
    const promises = booksBeans.map(async (bkBean) => {
      const response = await http.get(apiUrl + bkBean.id);
      let data = response.data.volumeInfo;
      let bk: BookView = {
        id: response.data.id,
        authors: data.authors,
        title: data.title,
        description: cleanHtmlTags(data.description),
        thumbnail: data.imageLinks.thumbnail,
        genres: data.categories,
        publisher: data.publisher,
        status: bkBean.status,
      };
      return bk;
    });

    // Attendere il completamento di tutte le promesse
    bookViews = await Promise.all(promises);
    filter(currentFilter, currentAscendingOrder);
  };

  // Chiamare get_books_view() al caricamento della pagina
  axios
    .get(`http://localhost:8080/list/${userID}`)
    .then((res: AxiosResponse) => {
      if (res.status == 200) {
        booksBeans = res.data;
        get_books_view(); // Chiamare la funzione per ottenere la vista dei libri
      }
    });

  const toggleMinimalView = () => {
    if (minimalView) {
      minimalView = false;
      localStorage.setItem("view", "bookshelf");
    } else {
      minimalView = true;
      localStorage.setItem("view", "minimal");
    }
  };

  const logout = () => {
    localStorage.removeItem("userID");
    localStorage.removeItem("view");
    window.location.href = "http://localhost:3000/login";
  };

  const handleResearchChange = () => {
    foundBooks = [];
    if (research.length < 4) return;

    axios.get(`${apiUrl}?q=${research}`).then((response: AxiosResponse) => {
      let books = response.data.items;
      let newFoundBooks = [];
      books.forEach((book) => {
        let data = book.volumeInfo;
        if (!data?.imageLinks?.thumbnail) return;
        if (!data?.authors) return;
        let bk: Book = {
          id: book.id,
          authors: data.authors,
          title: data.title,
          thumbnail: data.imageLinks.thumbnail,
          publisher: data.publisher,
          description: data.description,
          genres: data.categories,
        };
        if (newFoundBooks.length < 10) newFoundBooks.push(bk);
      });
      foundBooks = newFoundBooks;
    });
  };

  const handleOrderChange = () => {
    currentAscendingOrder = currentAscendingOrder ? false : true;
    filter(currentFilter, currentAscendingOrder);
  };

  const handleFilterChange = () => {
    if (currentFilter == "title") currentFilter = "status";
    else currentFilter = "title";
    filter(currentFilter, currentAscendingOrder);
  };

  const filter = (key: string, ascendingOrder: boolean = true) => {
    if (key == "title") {
      bookViews = bookViews.sort((a, b) => a.title.localeCompare(b.title));
    } else if (key == "status") {
      bookViews = bookViews.sort((a, b) => a.status.localeCompare(b.status));
    }
    if (!ascendingOrder) {
      bookViews = bookViews.reverse();
    }
  };

  const handleBookRemoval = (id: string) => {
    axios.post(`http://localhost:8080/remove_book`, {
      data: {
        bookID: id,
        userID: userID,
      },
    });
    bookViews = bookViews.filter((a) => {
      return a.id != id;
    });
  };

  const handleBookAdd = (bk: Book, userID: string) => {
    axios.post(`http://localhost:8080/insert_book`, {
      data: {
        bookID: bk.id,
        userID: userID,
        status: "to read",
      },
    });
    let newBk: BookView = {
      id: bk.id,
      authors: bk.authors,
      title: bk.title,
      description: bk.description,
      thumbnail: bk.thumbnail,
      publisher: bk.publisher,
      genres: bk.genres,
      status: "to read",
    };
    bookViews = [...bookViews, newBk];
  };

  const isBookInList = (
    id: string,
    bookViews: BookView[]
  ): [boolean, status] => {
    let filtered = bookViews.find((o) => o.id == id);
    if (filtered) return [true, filtered.status];
    return [false, null];
  };
</script>

<home>
  <h1>Home</h1>
  <button class="main-btn" on:click={logout}>logout</button>
  <br /> <br />
  <input
    type="text"
    name="search"
    class="form-input"
    id="research-input"
    placeholder="im looking for... "
    bind:value={research}
    on:input={handleResearchChange}
  />

  {#if bookViews.length > 1 && !foundBooks.length}
    <br /> <br /> <br />
    <input
      type="button"
      class="main-btn"
      bind:value={currentFilter}
      on:click={handleFilterChange}
    />
    <input
      type="button"
      class="main-btn"
      value={currentAscendingOrder ? "˅" : "˄"}
      on:click={handleOrderChange}
    />
  {/if}

  <!-- messaggio di avviso che non sei loggato -->
  <!-- {#if !userID}<a href="/login"><p>i want my books to be saved</p></a>{/if} -->

  <!-- lista minimale (nascosta durante ricerca) -->
  {#if minimalView && bookViews.length && !foundBooks.length}
    <h2>My Bookshelf...</h2>
    <table class="book-table">
      {#each bookViews as bk, idx}
        <tr>
          <td class="book-table-row-number">{idx + 1}</td>
          <td>
            <a
              class="book-link"
              title={`${bk.title} (${bk.publisher || ""})`}
              href={`/book/${bk.id}`}
            >
              {bk.title}
            </a>
          </td>
          <td title={bk.authors.join(", ")}>{bk.authors.join(", ")}</td>
          <td class="book-table-row-status">{bk.status}</td>
          <td class="book-table-row-remove"
            ><button on:click={() => handleBookRemoval(bk.id)}>-</button></td
          >
        </tr>
      {/each}
    </table>
  {/if}

  <!-- Cambia vista (nascosta durante ricerca) -->
  {#if bookViews.length || foundBooks.length}
    <br /><br />
    <button class="main-btn" on:click={toggleMinimalView}>Change view</button>
  {/if}

  <!-- libri della lista (nascosti durante ricerca) -->
  {#if bookViews.length && !research && !minimalView}
    <br /> <br />
    <h2>My Bookshelf...</h2>
    <br />
    <div class="book-card-container">
      {#each bookViews as bk}
        <div class="book-card">
          <BookC {bk} singlePage={false}></BookC>
        </div>
      {/each}
    </div>
  {/if}

  <!-- libreria vuota (nascosta durante ricerca) -->
  {#if !bookViews.length && !foundBooks.length}
    <br /> <br />
    <h3>My Library is empty...</h3>
  {/if}

  <!-- libri trovati -->
  {#if foundBooks.length && !minimalView}
    <br /> <br /><br />
    <div class="book-card-container">
      {#each foundBooks as bk}
        <div class="book-card">
          <SearchResultC {bk} bkStatus={isBookInList(bk.id, bookViews)[1]}
          ></SearchResultC>
        </div>
      {/each}
    </div>
  {/if}

  {#if foundBooks.length && minimalView}
    <table class="book-table">
      {#each foundBooks as bk, idx}
        <tr>
          <td class="book-table-row-number">{idx + 1}</td>
          <td>
            <a
              class="book-link"
              title={`${bk.title} (${bk.publisher || ""})`}
              href={`/book/${bk.id}`}
            >
              {bk.title}
            </a>
          </td>
          <td title={bk.authors.join(", ")}>{bk.authors.join(", ")}</td>
          <td>
            {#if isBookInList(bk.id, bookViews)[0]}
              {isBookInList(bk.id, bookViews)[1]}
              <button on:click={() => handleBookRemoval(bk.id)}>-</button>
            {:else}
              <button on:click={() => handleBookAdd(bk, userID)}>+</button>
            {/if}
          </td>
        </tr>
      {/each}
    </table>
  {/if}
  <br /><br /><br /><br /><br /> <br /><br /><br /><br />
</home>
