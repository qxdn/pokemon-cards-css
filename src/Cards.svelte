<script>
	
	import { activeCard } from "./lib/stores/activeCard.js";
	
	let thisGrid;
	
	$: active = thisGrid && thisGrid.contains( $activeCard );
	
</script>

<section 
	class="card-grid" 
	class:active
	bind:this={thisGrid}
>

<slot />

</section>

<style>
	.card-grid {
		display: grid;
		grid-template-columns: 1fr;
		grid-gap: 50px 2vw;
		transform-style: preserve-3d;
		height: 100%;
		max-width: 1200px;
		margin: auto;
		padding: 50px;
		position: relative;
	}
	
	.card-grid.active {
		z-index: 99;
	}
		
	@media screen and (min-width: 900px) {
		.card-grid {
			grid-template-columns: 1fr 1fr 1fr;
		}
	}
	
	
	@media screen and (max-width: 900px) {
		
		:global( .card-grid > .card ) {
			--row: 1;
			grid-column: 1;
			grid-row: var(--row);
			transition: opacity 0.2s ease, transform 0.2s ease;
		}

		:global( .card-grid > .card:nth-child(1n) ) {
			position: relative;
			left: -50px;
			top: 10px;
			z-index: calc(var(--card-scale) * 10 + 50);
			transform: translate3d(0, 0, 0.1px) rotateZ(-5deg);
			opacity: 1;
		}
		:global( .card-grid > .card:nth-child(2n) ) {
			left: 0px;
			top: -10px;
			z-index: calc(var(--card-scale) * 10 + 49);
			transform: translate3d(0, 0, 0.1px) rotateZ(0deg);
			opacity: 0.99;
		}
		:global( .card-grid > .card:nth-child(3n) ) {
			left: 50px;
			top: 0px;
			z-index: calc(var(--card-scale) * 10 + 48);
			transform: translate3d(0, 0, 0.1px) rotateZ(5deg);
			opacity: 0.99;
		}
		:global( .card-grid > .card.interacting) ,
		:global( .card-grid > .card.active ) {
			opacity: 1;
		}
		
		:global( .card-grid > .card:nth-child(n+4):nth-child(-n+6) ) { grid-row: 2; }
		:global( .card-grid > .card:nth-child(n+7):nth-child(-n+9) ) { grid-row: 3; }
		:global( .card-grid > .card:nth-child(n+10):nth-child(-n+12) ) { grid-row: 4; }
		:global( .card-grid > .card:nth-child(n+13):nth-child(-n+15) ) { grid-row: 5; }
		:global( .card-grid > .card:nth-child(n+16):nth-child(-n+18) ) { grid-row: 6; }
		:global( .card-grid > .card:nth-child(n+19):nth-child(-n+21) ) { grid-row: 7; }
		:global( .card-grid > .card:nth-child(n+22):nth-child(-n+24) ) { grid-row: 8; }
		:global( .card-grid > .card:nth-child(n+25):nth-child(-n+27) ) { grid-row: 9; }
		:global( .card-grid > .card:nth-child(n+28):nth-child(-n+30) ) { grid-row: 10; }
		:global( .card-grid > .card:nth-child(n+31):nth-child(-n+33) ) { grid-row: 11; }
		:global( .card-grid > .card:nth-child(n+34):nth-child(-n+36) ) { grid-row: 12; }
		:global( .card-grid > .card:nth-child(n+37):nth-child(-n+39) ) { grid-row: 13; }
		:global( .card-grid > .card:nth-child(n+40):nth-child(-n+42) ) { grid-row: 14; }
		:global( .card-grid > .card:nth-child(n+43):nth-child(-n+45) ) { grid-row: 15; }
		:global( .card-grid > .card:nth-child(n+46):nth-child(-n+48) ) { grid-row: 16; }
		:global( .card-grid > .card:nth-child(n+49):nth-child(-n+51) ) { grid-row: 17; }
		:global( .card-grid > .card:nth-child(n+52):nth-child(-n+54) ) { grid-row: 18; }
		:global( .card-grid > .card:nth-child(n+55):nth-child(-n+57) ) { grid-row: 19; }
		:global( .card-grid > .card:nth-child(n+58):nth-child(-n+60) ) { grid-row: 20; }
		:global( .card-grid > .card:nth-child(n+61):nth-child(-n+63) ) { grid-row: 21; }
		:global( .card-grid > .card:nth-child(n+64):nth-child(-n+66) ) { grid-row: 22; }
		:global( .card-grid > .card:nth-child(n+67):nth-child(-n+69) ) { grid-row: 23; }
		:global( .card-grid > .card:nth-child(n+70):nth-child(-n+72) ) { grid-row: 24; }
		:global( .card-grid > .card:nth-child(n+73):nth-child(-n+75) ) { grid-row: 25; }
		:global( .card-grid > .card:nth-child(n+76):nth-child(-n+78) ) { grid-row: 26; }
		:global( .card-grid > .card:nth-child(n+79):nth-child(-n+81) ) { grid-row: 27; }
		:global( .card-grid > .card:nth-child(n+82):nth-child(-n+84) ) { grid-row: 28; }
		:global( .card-grid > .card:nth-child(n+85):nth-child(-n+87) ) { grid-row: 29; }
		:global( .card-grid > .card:nth-child(n+88):nth-child(-n+90) ) { grid-row: 30; }
		:global( .card-grid > .card:nth-child(n+91):nth-child(-n+93) ) { grid-row: 31; }
		:global( .card-grid > .card:nth-child(n+94) ) {
			grid-row: auto;
			grid-column: auto;
			transform: none!important;
			left: 0!important;
			top: 0!important;
		}

	}

	@media screen and (min-width: 600px) and (max-width: 900px) {
		.card-grid {
			max-width: 420px;
			margin: auto;
		}
		:global( .card-grid > .card:nth-child(1n) ) {
			left: -100px;
			top: 10px;
			transform: translate3d(0, 0, 0.1px) rotateZ(-5deg);
		}
		:global( .card-grid > .card:nth-child(2n) ) {
			left: 0px;
			top: -10px;
			transform: translate3d(0, 0, 0.1px) rotateZ(0deg);
		}
		:global( .card-grid > .card:nth-child(3n) ) {
			left: 100px;
			top: 0px;
			transform: translate3d(0, 0, 0.1px) rotateZ(5deg);
		}
	}

	:global( .card-grid > .card.active ) {
		transform: translate3d(0, 0, 0.1px)!important;
	}
	
</style>
