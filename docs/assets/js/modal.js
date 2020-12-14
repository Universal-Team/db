document.getElementById("modal").addEventListener("show.bs.modal", function(event) {
	let button = event.relatedTarget;

	this.querySelector(".modal-title").innerText = button.getAttribute("data-name");
	if(button.getAttribute("data-path")) {
		this.querySelector(".modal-body").innerHTML = "<img class='qr-image' alt='QR code for " + button.getAttribute("data-name") + "' src='" + button.getAttribute("data-path") + "'>";
		this.querySelector(".modal-dialog").classList.remove("modal-lg");
	} else if(button.getAttribute("data-content")) {
		this.querySelector(".modal-body").innerHTML = button.getAttribute("data-content");
		this.querySelector(".modal-dialog").classList.add("modal-lg");
	}
});
