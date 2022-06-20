function search(query) {
	// Fuzzy search, allows anything between letters and space, hyphen, and underscore are treated the same
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

	// Write to URL
	if(query !== "")
		searchParams.set("q", query);
	else
		searchParams.delete("q");
	var paramString = searchParams.toString();
	if(paramString !== "")
		paramString = "?" + paramString;
	history.replaceState(null, "", window.location.pathname + paramString + window.location.hash);
}

// Load search from GET var
var searchParams = new URLSearchParams(window.location.search);
if(searchParams.has("q")) {
	document.getElementById("search").value = searchParams.get("q");
	search(searchParams.get("q"));
}
