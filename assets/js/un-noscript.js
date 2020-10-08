Array.from(document.getElementsByClassName("back-link")).forEach(r => {
	if(window.history.length > 1)
		r.href = "javascript:window.history.back()";
});

Array.from(document.getElementsByClassName("qr-link")).forEach(r => {
	r.href = "javascript:toggleQR('" + r.dataset.path + "','" + r.dataset.name + "');";
});

Array.from(document.getElementsByClassName("script-show")).forEach(r => {
	r.classList.remove("d-none");
});
