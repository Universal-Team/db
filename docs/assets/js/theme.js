function loadTheme() {
	const themeCSS = document.getElementById("theme-css");
	const today = new Date();
	if(today.getMonth() == 3 && today.getDate() == 1) {
		themeCSS.href = "/assets/css/83-percent.css";
	} else {
		if(!localStorage.theme || localStorage.theme == "default") {
			themeCSS.href = "/assets/css/style.css";
			window.addEventListener("prefersColorScheme", event => console.log(event));
			var darkMatch = window.matchMedia("(prefers-color-scheme: dark)");
			darkMatch.addEventListener("change", match => {
				document.documentElement.dataset.bsTheme = match.matches ? "dark" : "light";
			})

			document.documentElement.dataset.bsTheme = darkMatch.matches ? "dark" : "light";
		} else {			
			themeCSS.href = "/assets/css/" + localStorage.theme + ".css";
			document.documentElement.dataset.bsTheme = localStorage.theme == "dark" ? "dark" : "light";
		}
	}
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
