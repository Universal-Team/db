const labels = {
	year:   31536000,
	month:  2592000,
	week:   604800,
	day:    86400,
	hour:   3600,
	minute: 60,
	second: 1
};

let relativeTime, now;

function timeDifference(now, then) {
	let dif = Math.round((now - then) / 1000);

	for(let label in labels) {
		if(Math.abs(dif) > labels[label] || label == "second") {
			return relativeTime.format(-Math.round(dif / labels[label]), label);
		}
	}
}

function updateDates() {
	relativeTime = new Intl.RelativeTimeFormat(document.documentElement.lang, {numeric: "auto"});
	now = new Date();

	for(let elem of document.getElementsByTagName("time")) {
		const date = new Date(elem.dateTime);
		elem.innerText = timeDifference(now, date);
		elem.title = date.toLocaleString(document.documentElement.lang);
	}
}

updateDates();
