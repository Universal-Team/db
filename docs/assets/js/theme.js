function loadTheme() {
	const themeCSS = document.getElementById("theme-css");
	if(!localStorage.theme || localStorage.theme == "default")
		themeCSS.href = "/assets/css/style.css";
	else
		themeCSS.href = "/assets/css/" + localStorage.theme + ".css";
}

function setTheme(theme) {
	if(theme == "default")
		delete localStorage.theme;
	else
		localStorage.theme = theme;
	loadTheme();
}

loadTheme();

window.onload = function() {
	if(localStorage.theme)
		document.getElementById("themeSelector").value = localStorage.theme;
}
