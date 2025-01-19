<script>
  import { onMount } from "svelte";

  import CardList from "./Cards.svelte";
  import Card from "./lib/components/CardProxy.svelte";
  import Deck from "./Deck.svelte";

  let showcase,
    decks;

  let query = "";
  let isLoading = true;

  const getCards = async () => {
    let promiseArray = [];
    let cardFetch = await fetch("/data/cards.json");
    let cards = await cardFetch.json();
    return cards;
  };

  const loadCards = async () => {
    return getCards().then((cards) => {
      //window.cards = cards;
      showcase = cards.showcase;
      decks = cards.decks;
      isLoading = false;
    });
  };

  onMount(() => {
    loadCards();
    const $headings = document.querySelectorAll("h1,h2,h3");
    const $anchor = [...$headings].filter((el) => {
      const id = el.getAttribute("id")?.replace(/^.*?-/g, "");
      const hash = window.location.hash?.replace(/^.*?-/g, "");
      return id === hash;
    })[0];
    if ($anchor) {
      setTimeout(() => {
        $anchor.scrollIntoView();
      }, 100);
    }
  });
</script>

<main>
  <header>
    <h1 id="⚓-top">我的YGO卡组 <sup>V0</sup></h1>

    <section class="intro" id="⚓-intro">
      <p>
       我在YGO的其中一幅蛇眼卡组，采用<a href="https://github.com/simeydotme">simeydotme</a>的<a href="https://github.com/simeydotme/pokemon-cards-css">pokemon-cards-css</a>实现
      </p>
    </section>

    <div class="showcase">
      {#if !showcase}
        loading...
      {:else}
        <Card
          id={showcase.id}
          name={showcase.name}
          set={showcase.set}
          number={showcase.number}
          types={showcase.types}
          supertype={showcase.supertype}
          subtypes={showcase.subtypes}
          rarity={showcase.rarity}
          isReverse={showcase.isReverse}
          showcase={true}
          img={showcase.images}
        />
      {/if}
    </div>

    <section class="info">
      <h2>点击放大卡片</h2>

      <hr />

      <p class="small">
       右边这张卡片，你觉得她的原卡是哪张呢

      <br/>
      <a href="https://github.com/qxdn/pokemon-cards-css/tree/ygo">source code</a>
      </p>
    </section>
  </header>


  {#if isLoading}
      loading...
  {:else}
    {#each decks as deck}
    <h2 id="⚓-deck">
      <a href="#⚓-deck"> 卡组 </a>
    </h2>
      <Deck
        mainDeck={deck.main}
        extraDeck={deck.extra}
        sideDeck={deck.side}
        isLoading={isLoading}
      />
    {/each}
  {/if}
  
  

</main>

<div class="back-to-top">
  <a href="#⚓-top">Back to Top</a>
</div>

<style>
  .back-to-top a {
    color: inherit;
    text-decoration: none;
    z-index: 999;
  }
</style>
