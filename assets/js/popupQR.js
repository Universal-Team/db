function toggleQR(path, name) {
	if(path)
		document.getElementById("popup-image").src = path;
	if(name)
		document.getElementById("popup-label").textContent = name;
	let container = document.getElementById("popup-container");
	container.style.display = "";
	container.classList.toggle("d-none");
}
