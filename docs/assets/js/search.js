function search(query) {
	let regex = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\\?./g, "$&.*").replace(/[-_ ]/, "[-_ ]"), "gi");
	Array.from(document.getElementById("card-container").children).forEach(function(r) {
		let card = r.children[0];
		for(let item in card.dataset) {
			if(item == "title" ? card.dataset[item].match(regex) : card.dataset[item].toLowerCase().includes(query.toLowerCase()))
				return r.classList.remove("d-none");
		}
		r.classList.add("d-none");
	});
}
