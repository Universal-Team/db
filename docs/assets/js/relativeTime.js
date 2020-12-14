const lengths = [1, 60, 3600, 86400, 604800, 2592000, 31536000, Infinity];
const labels = ["", "second", "minute", "hour", "day", "week", "month", "year"];

function timeDifference(now, then) {
	let dif = Math.round((now - then) / 1000);

	for(let i in lengths) {
		if(dif < lengths[i]) {
			return Math.round(dif / lengths[i - 1]) + " " + labels[i] + (Math.round(dif / lengths[i - 1]) == 1 ? "" : "s") + " ago";
		}
	}
}

for(let i = 0; i < document.getElementsByTagName("time").length; i++) {
	let elem = document.getElementsByTagName("time")[i];
	let date = new Date(elem.dateTime);
	elem.innerText = timeDifference(new Date(), date);
	elem.title = date.toLocaleString();
}
