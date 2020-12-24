function search(query) {
	Array.from(document.getElementById("card-container").children).forEach(function(r) {
		let card = r.children[0];
		for(let item in card.dataset) {
			if(card.dataset[item].toLowerCase().includes(query.toLowerCase()))
				return r.classList.remove("d-none");
		}
		r.classList.add("d-none");
	});
}
