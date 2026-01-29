const labels = {
	year:   31536000,
	month:  2592000,
	week:   604800,
	day:    86400,
	hour:   3600,
	minute: 60,
	second: 1
};

var relativeTime = null, now;

function timeDifference(now, then) {
	const dif = Math.round((now - then) / 1000);

	for(label in labels) {
		if(Math.abs(dif) > labels[label] || label == "second") {
			if(relativeTime) {
				return relativeTime.format(-Math.round(dif / labels[label]), label);
			} else {
				const amount = Math.round(dif / labels[label]);
				return amount + " " + label + (amount == 1 ? " ago" : "s ago");
			}
		}
	}
}

function updateDates() {
	if(typeof Intl !== "undefined" && Intl.RelativeTimeFormat)
		relativeTime = new Intl.RelativeTimeFormat(document.documentElement.lang, {numeric: "auto"});
	now = new Date();

	const times = document.getElementsByTagName("time");
	for(i = 0; i < times.length; i++) {
		const elem = times[i];
		const date = new Date(elem.getAttribute("datetime"));
		elem.innerText = timeDifference(now, date);
		elem.title = date.toLocaleString(document.documentElement.lang);
	}
}

updateDates();
