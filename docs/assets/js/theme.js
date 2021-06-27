function loadTheme() {
	const themeCSS = document.getElementById("themeCSS");
	if(!localStorage.theme || localStorage.theme == "default") {
		if(themeCSS)
			themeCSS.remove();
	} else {
		if(themeCSS) {
			themeCSS.href = "/assets/css/" + localStorage.theme +".css";
		} else {
			const l = document.createElement("link");
			l.rel = "stylesheet";
			l.type = "text/css";
			l.media = "screen";
			l.href = "/assets/css/" + localStorage.theme +".css"
			l.id = "themeCSS";
		
			document.head.appendChild(l);
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
