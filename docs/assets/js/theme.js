function loadTheme() {
	if(!localStorage.theme || localStorage.theme == "default") {
		document.getElementById("themeCSS")?.remove();
	} else {
		if(document.getElementById("themeCSS")) {
			document.getElementById("themeCSS").href = `/assets/css/${localStorage.theme}.css`;
		} else {
			let l = document.createElement("link");
			l.rel = "stylesheet";
			l.type = "text/css";
			l.media = "screen";
			l.href = `/assets/css/${localStorage.theme}.css`
			l.id = "themeCSS";
		
			document.head.appendChild(l);
		}
	}

}

function setTheme(theme) {
	localStorage.theme = theme;
	loadTheme();
}

loadTheme();

window.onload = () => {
	if(localStorage.theme)
		document.getElementById("themeSelector").value = localStorage.theme;
}
