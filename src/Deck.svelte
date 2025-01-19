<script>
  import CardList from "./Cards.svelte";
  import Card from "./lib/components/CardProxy.svelte";

  export let mainDeck = []; // 主卡组
  export let extraDeck = []; // 额外卡组
  export let sideDeck = []; // 副卡组
  export let isLoading = true;
  export let allOpen = true;
  export let mainOpen = true;
  export let extraOpen = true;
  export let sideOpen = true;

  function isOpen(deck, all, open) {
    // 如果没有卡组
    if (!isArray(deck)) {
      return false;
    }
    // 如果卡组为空
    if (deck.length === 0) {
      return false;
    }
    if (isDefined(all)) {
      return all;
    }
    return open;
  }

  function isDefined(v) {
    return typeof v !== "undefined" && v !== null;
  }

  function isArray(v) {
    return typeof v !== "undefined" && Array.isArray(v);
  }

  //
  mainOpen = isOpen(mainDeck, allOpen, mainOpen);
  extraOpen = isOpen(extraDeck, allOpen, extraOpen);
  sideOpen = isOpen(sideDeck, allOpen, sideOpen);

</script>

<h2 >
  主卡组
</h2>
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
 
    <h2 >
      额外卡组
    </h2>
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
 
    <h2 >
       副卡组
    </h2>
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