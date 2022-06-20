var match = window.location.pathname.match(/^(\/3?ds\/)([\w\d\s-_]+)/);
if(match) {
	document.getElementById("search-form").action = match[1];
	document.getElementById("search").value = match[2];
}
