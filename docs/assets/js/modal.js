function updateModal(event) {
	// console.log(event);
	const button = event.relatedTarget || event.srcElement;
	const modal = document.getElementById("modal");

	// console.log(button, modal);

	modal.querySelector(".modal-title").innerText = button.getAttribute("data-name");
	if(button.getAttribute("data-path")) {
		modal.querySelector(".modal-dialog").classList.remove("modal-lg");
		modal.querySelector(".modal-body").innerHTML =
				'<div class="mx-auto text-center"><img class="qr-image" alt="QR code for ' + button.getAttribute("data-name") + '" src="' + button.getAttribute("data-path") + '">' +
				'<p class="mt-3">' + (button.getAttribute("data-name").endsWith(".cia") ? strings["scan-qr-fbi"] : strings["scan-qr-dsidl"]) + "</p></div>";
	} else if(button.getAttribute("data-content")) {
		modal.querySelector(".modal-dialog").classList.add("modal-lg");
		modal.querySelector(".modal-body").innerHTML = button.getAttribute("data-content");
	}
}

document.getElementById("modal").addEventListener("show.bs.modal", updateModal);
