<script lang="ts">
  import axios, { AxiosError, type AxiosResponse } from "axios";
  import BookC from "./BookC.svelte";
  import type { BookView, status } from "../Book";

  export let bookID: string;

  const userID =
    localStorage.getItem("userID") ||
    (location.href = "http://localhost:3000/login");

  let bkView: BookView;
  let bookCurrentStatus: status;
  let bookStatuses: any[] = [];

  const apiUrl = "https://www.googleapis.com/books/v1/volumes/";

  const cleanHtmlTags = (input: string) => input?.replaceAll(/<[^>]*>/g, "");

  axios.get(apiUrl + bookID).then((res: AxiosResponse) => {
    let data = res.data.volumeInfo;
    bkView = {
      id: bookID,
      authors: data.authors,
      title: data.title,
      thumbnail: data.imageLinks.thumbnail,
      publisher: data.publisher,
      description: cleanHtmlTags(data.description),
      genres: data.categories,
      status: null,
    };
    axios
      .get(`http://localhost:8080/book/${bookID}/${userID}`)
      .then((res: AxiosResponse) => {
        if (res.status == 200) {
          bkView.status = res.data.bookStatus;
          bookCurrentStatus = bkView.status;
        }
      });
    console.log(bkView);
  });

  axios
    .get(`http://localhost:8080/book/${bookID}/${userID}`)
    .then((res: AxiosResponse) => {
      if (res.status == 200) {
        bookCurrentStatus = res.data.book_status;
        refresh_statusses();
      }
    })
    .catch((error: AxiosError) => {
      if (error.response.status == 404) {
        bookCurrentStatus = null;
        refresh_statusses();
      }
    });

  const refresh_statusses = () => {
    bookStatuses = [
      bookCurrentStatus,
      "to read",
      "reading",
      "finished",
      "paused",
    ];
    bookStatuses = bookStatuses.filter(
      (item, index) => bookStatuses.indexOf(item) === index
    );
  };

  const handleStatusChange = (e: Event) => {
    if (!bookCurrentStatus) (e.target as HTMLInputElement).value = "to read"; // se aggiungo il libro, chiaramente ha lo stato settato a null
    bookCurrentStatus = bkView.status = (e.target as HTMLInputElement)
      .value as status;
    refresh_statusses();
    axios.post(`http://localhost:8080/insert_book`, {
      data: {
        bookID: bookID,
        userID: userID,
        status: bookCurrentStatus,
      },
    });
  };

  const handleListRemoval = () => {
    bookCurrentStatus = bkView.status = null;
    refresh_statusses();

    axios.post(`http://localhost:8080/remove_book`, {
      data: {
        bookID: bookID,
        userID: userID,
      },
    });
  };
</script>

<book-page>
  <BookC bk={bkView} singlePage={true}></BookC>

  {#if bkView && !bkView.status}
    <button class="main-btn" on:click={handleStatusChange}
      >Add To my List</button
    >
  {:else if bkView && bkView.status}
    <select
      value={bookCurrentStatus == null ? "Add to List" : bookCurrentStatus}
      on:change={handleStatusChange}
    >
      {#each bookStatuses as status}
        {#if status}
          <option>{status}</option>
        {/if}
      {/each}
    </select>
    <button class="main-btn" on:click={handleListRemoval}
      >Remove from my list</button
    >
  {/if}

  <br /> <br />
  <a href="/home">Go To Home Page</a>
  <br /><br /><br /> <br /> <br />
</book-page>
