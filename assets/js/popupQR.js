function toggleQR(path, name) {
	let image = document.getElementById("popup-image");
	if(!image) {
		if(path) {
			let img = document.createElement("img");
			img.src = path;
			img.classList = "mx-auto d-block";
			img.id = "popup-image";
			img.alt = name ? ("QR code for " + name) : "QR code";
			document.getElementById("popup").appendChild(img);
			document.getElementById("popup-container").classList.remove("d-none");
		}
		document.getElementById("popup-label").textContent = name ?? "";
	} else {
		image.remove();
		document.getElementById("popup-container").classList.add("d-none");
	}
}
