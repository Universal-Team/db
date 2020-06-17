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
	let row = document.createElement("div");
	row.classList = "row mb-3";
	for(let i in sorted) {
		let col = document.createElement("div");
		col.classList.add("col-md-3");
		col.appendChild(sorted[i]);
		row.appendChild(col);
		if(i % 4 == 3) {
			container.appendChild(row);
			row = document.createElement("div");
			row.classList = "row mb-3";
		}
	}
	container.appendChild(row);
}
