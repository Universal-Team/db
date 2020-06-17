if(localStorage.theme)
	document.getElementById("theme").href = `/assets/css/${localStorage.theme}.css`;

function changeTheme() {
	if(localStorage.theme == "dark") // Change to light
		localStorage.theme = "light";
	else // Change to dark
		localStorage.theme = "dark";

	// Update active stylesheet
	document.getElementById("theme").href = `/assets/css/${localStorage.theme}.css`;
}
