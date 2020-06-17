function search(query) {
	Array.from(document.getElementsByClassName("card")).forEach(function(r) {
		if(r.id.toLowerCase().includes(query.toLowerCase()))
			r.classList.remove("d-none");
		else
			r.classList.add("d-none");
	});
}
