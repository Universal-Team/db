document.getElementById("qrModal").addEventListener("show.bs.modal", function(event) {
	let button = event.relatedTarget;

	this.querySelector(".modal-title").innerText = button.getAttribute("data-name");
	this.querySelector(".modal-body").innerHTML = "<img class='qr-image' alt='QR code for " + button.getAttribute("data-name") + "' src='" + button.getAttribute("data-path") + "'>";
});
