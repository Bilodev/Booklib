<script lang="ts">
  import type { BookView } from "../Book";

  export let bk: BookView;
  export let singlePage: boolean;
</script>

<book>
  {#if bk}
    <div>
      <h2>{bk.authors.join(", ")} - {bk.title}</h2>
      <h5>({bk.publisher})</h5>
      {#if singlePage}
        <p>{bk.genres ? `${bk.genres?.join(", ")}` : ""}</p>
        <p>{bk.description || "No Descritption Provided"}</p>
      {/if}
      <a href="/book/{bk.id}"><img src={bk.thumbnail} alt="Book Thumbnail" /></a
      >
      <p>
        {#if bk.status && !singlePage}
          {bk.status != "finished" && bk.status != "to read" ? "Currently" : ""}
          {bk.status}
        {/if}
      </p>
    </div>
  {/if}
</book>
