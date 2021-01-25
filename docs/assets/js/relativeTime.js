const labels = {
	year:   31536000,
	month:  2592000,
	week:   604800,
	day:    86400,
	hour:   3600,
	minute: 60,
	second: 1
};

const relativeTime = new Intl.RelativeTimeFormat(navigator.language, {numeric: "auto"});

function timeDifference(now, then) {
	let dif = Math.round((now - then) / 1000);

	for(let label in labels) {
		if(Math.abs(dif) > labels[label] || label == "second") {
			return relativeTime.format(-Math.round(dif / labels[label]), label);
		}
	}
}

for(let i = 0; i < document.getElementsByTagName("time").length; i++) {
	let elem = document.getElementsByTagName("time")[i];
	let date = new Date(elem.dateTime);
	elem.innerText = timeDifference(new Date(), date);
	elem.title = date.toLocaleString();
}
