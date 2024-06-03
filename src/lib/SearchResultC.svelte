<script lang="ts">
  import type { Book, status } from "../Book";

  export let bk: Book;
  export let status: status;
  console.log(status);
</script>

<found-book>
  {#if bk && bk.thumbnail}
    <div>
      <p class="book-title">{bk.authors.join(", ")} - {bk.title}</p>
      <h5>{status || ""}</h5>
      <a href="/book/{bk.id}">
        <img src={bk.thumbnail} alt="Book Thumbnail" />
      </a>
      <p class="book-author">{bk.publisher || ""}</p>
    </div>
  {/if}
</found-book>
