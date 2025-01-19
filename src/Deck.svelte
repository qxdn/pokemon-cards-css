<script>
  import CardList from "./Cards.svelte";
  import Card from "./lib/components/CardProxy.svelte";

  export let mainDeck = []; // 主卡组
  export let extraDeck = []; // 额外卡组
  export let sideDeck = []; // 副卡组
  export let isLoading = true;
</script>

<CardList>
  {#if isLoading}
    loading...
  {:else}
    {#each mainDeck as card, index}
      <Card
        id={card.id}
        name={card.name}
        number={card.number}
        set={card.set}
        types={card.types}
        supertype={card.supertype}
        subtypes={card.subtypes}
        rarity={card.rarity}
        img={card.images}
      />
    {/each}
  {/if}
</CardList>

<CardList>
  {#if isLoading}
    loading...
  {:else}
    {#each extraDeck as card, index}
      <Card
        id={card.id}
        name={card.name}
        number={card.number}
        set={card.set}
        types={card.types}
        supertype={card.supertype}
        subtypes={card.subtypes}
        rarity={card.rarity}
        img={card.images}
      />
    {/each}
  {/if}
</CardList>

<CardList>
  {#if isLoading}
    loading...
  {:else}
    {#each sideDeck as card, index}
      <Card
        id={card.id}
        name={card.name}
        number={card.number}
        set={card.set}
        types={card.types}
        supertype={card.supertype}
        subtypes={card.subtypes}
        rarity={card.rarity}
        img={card.images}
      />
    {/each}
  {/if}
</CardList>
