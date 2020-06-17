function search(query) {
	Array.from(document.getElementById("card-container").children).forEach(function(r) {
		if(r.id.toLowerCase().includes(query.toLowerCase()))
			r.classList.remove("d-none");
		else
			r.classList.add("d-none");
	});
}

if(!localStorage.sortDirection)
	localStorage.sortDirection = false;
if(!localStorage.sortProp)
	localStorage.sortProp = "title";

document.getElementById("sort-direction").innerText = parseInt(localStorage.sortDirection) ? "Descending" : "Ascending";
sort();

function toggleSortDirection() {
	localStorage.sortDirection ^= 1;
	document.getElementById("sort-direction").innerText = parseInt(localStorage.sortDirection) ? "Descending" : "Ascending";
	sort();
}

function sort(prop) {
	if(prop)
		localStorage.sortProp = prop;

	let sorted = Array.from(document.getElementById("card-container").children).sort(function(l, r) {
		return ((l.dataset[localStorage.sortProp].toLowerCase() < r.dataset[localStorage.sortProp].toLowerCase()) ^ localStorage.sortDirection) ? -1 : 1;
	});
	document.getElementById("card-container").innerHTML = "";
	sorted.forEach(r => document.getElementById("card-container").appendChild(r));
}
