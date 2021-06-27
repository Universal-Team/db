function search(query) {
	const regex = new RegExp(query.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&").replace(/\\?./g, "$&.*").replace(/\\-|_| /g, "[-_ ]"), "gi");
	const cards = document.getElementById("card-container").children;
	for(i = 0; i < cards.length; i++) {
		const card = cards[i];
		card.classList.add("d-none");
		for(item in card.children[0].dataset) {
			if(item == "title" ? card.children[0].dataset[item].match(regex) : card.children[0].dataset[item].toLowerCase().match(query.toLowerCase())) {
				card.classList.remove("d-none");
				break;
			}
		}
	}
}
