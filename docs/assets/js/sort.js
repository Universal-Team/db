if(!localStorage.sortDirection)
	localStorage.sortDirection = 1;
if(!localStorage.sortProp)
	localStorage.sortProp = "updated";

document.getElementById("sort-" + localStorage.sortProp).classList.add("btn-secondary");
document.getElementById("sort-" + localStorage.sortProp).classList.remove("btn-outline-secondary");
document.getElementById("sort-direction").innerText = parseInt(localStorage.sortDirection) ? "Descending" : "Ascending";
sort();

function toggleSortDirection() {
	localStorage.sortDirection ^= 1;
	document.getElementById("sort-direction").innerText = parseInt(localStorage.sortDirection) ? "Descending" : "Ascending";
	sort();
}

function sort(prop) {
	if(prop) {
		document.getElementById("sort-" + prop).classList.remove("btn-outline-secondary");
		document.getElementById("sort-" + prop).classList.add("btn-secondary");
		document.getElementById("sort-" + localStorage.sortProp).classList.add("btn-outline-secondary");
		document.getElementById("sort-" + localStorage.sortProp).classList.remove("btn-secondary");
		localStorage.sortProp = prop;
	}

	let sorted = Array.from(document.getElementsByClassName("card")).sort(function(l, r) {
		return ((l.dataset[localStorage.sortProp].toLowerCase() < r.dataset[localStorage.sortProp].toLowerCase()) ^ localStorage.sortDirection) ? -1 : 1;
	});
	let container = document.getElementById("card-container");
	container.innerHTML = "";
	sorted.forEach(function(r) {
		let col = document.createElement("div");
		col.classList = "col mb-3";
		col.appendChild(r);
		container.appendChild(col);
	});
}
