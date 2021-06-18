---
---

const i18n = {
	{%- for i18n in site.data.i18n -%}
		{%- for lang in site.data.languages -%}
			{%- if lang[1].id == i18n[0] -%}
				"{{ i18n[0] }}": {
					"dir": "{{ lang[1].dir | default: "ltr" }}",
					{%- if lang[1] contains "crowdin" -%}"crowdin": "{{ lang[1].crowdin }}",{%- endif -%}
					{%- if lang[1] contains "proper-id" -%}"properId": "{{ lang[1].proper-id }}",{%- endif -%}
					"strings": {
						{%- for item in i18n[1] -%}
							"{{ item[0] | replace: '"', '\"' }}":"{{ item[1] | replace: '"', '\"' }}"{% unless forloop.last %},{% endunless %}
						{%- endfor -%}
					}
				},
			{%- endif -%}
		{%- endfor -%}
	{%- endfor -%}
};

var _jipt = [];

loadHead();

function loadHead(lang) {
	let languageID = lang || getLang();

	document.documentElement.lang = i18n[languageID].properId || languageID;
	document.documentElement.dir = i18n[languageID].dir;
	if(document.dir == "rtl") {
		document.getElementById("bootstrap-stylesheet").integrity = "sha384-mUkCBeyHPdg0tqB6JDd+65Gpw5h/l8DKcCTV2D2UpaMMFd7Jo8A+mDAosaWgFBPl";
		document.getElementById("bootstrap-stylesheet").href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.rtl.min.css";
	} else {
		document.getElementById("bootstrap-stylesheet").integrity = "sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1";
		document.getElementById("bootstrap-stylesheet").href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
	}

	if(languageID == "ic-IC") {
		_jipt.push(['project', 'universal-db']);
		_jipt.push(['escape', function() {
			delete localStorage.language;
			location.reload();
		}]);

		let langCheck = setInterval(() => {
			let jipt = document.getElementsByClassName("crowdin-jipt");
			if(jipt && jipt.length > 4) {
				let selectedLang = jipt[4].contentWindow.document.getElementById("jipt-target-languages").value;
				clearInterval(langCheck);
				if(["he"].includes(selectedLang)) {
					document.dir = "rtl";
					let bootstrapStylesheet = document.getElementById("bootstrap-stylesheet");
					bootstrapStylesheet.integrity = "sha384-mUkCBeyHPdg0tqB6JDd+65Gpw5h/l8DKcCTV2D2UpaMMFd7Jo8A+mDAosaWgFBPl";
					bootstrapStylesheet.href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.rtl.min.css";
				}
			}
		}, 500);
		let script = document.createElement("script");
		script.src = "//cdn.crowdin.com/jipt/jipt.js";
		document.head.appendChild(script);
	}
}

function loadLang(initing) {
	let languageID = getLang();
	if(!languageID || (initing && languageID == "en-US"))
		return;

	if(!initing)
		loadHead(false, languageID);

	if(!(languageID in i18n))
		return console.warn("Language not found", languageID);

	for(let element of document.getElementsByClassName("i18n")) {
		for(let c of element.classList) {
			let match = c.match(/(innerHTML|title|placeholder|ariaLabel|data-(.*?))-(.*)/);
			if(match) {
				let str = i18n[languageID].strings[match[3]];
				if(str) {
					if(match[2])
						element.dataset[match[2]] = str.replace(/\${(.*)}/g, (full, capture) => element.dataset[capture]);
					else
						element[match[1]] = str.replace(/\${(.*)}/g, (full, capture) => element.dataset[capture]);
				} else {
					console.warn("Translation is missing string", match[3]);
				}
			}
		}
	}

	for(let element of document.getElementById("language-dropdown").children) {
		if(element.children[0].dataset.lang == languageID) {
			element.children[0].classList.add("active");
		} else {
			element.children[0].classList.remove("active");
		}
	}

	document.getElementById("translate-on-crowdin").href = `https://${i18n[languageID].crowdin || "www"}.crowdin.com/project/universal-db`;
}

function getLang() {
	if(localStorage.language)
		return localStorage.language;

	for(let wl of window.navigator.languages) {
		let l = Object.keys(i18n).find(r => r == `${wl.substr(0, 2)}-${wl.substr(3, 2).toUpperCase()}`);
		if(!l) // If no match for lang-COUNTRY, try just lang
			l = Object.keys(i18n).find(r => r.substr(0, 2) == wl.substr(0, 2));
		if(l)
			return languageID = `${l.substr(0, 2)}-${l.substr(3, 3).toUpperCase()}`;
	}
}

function setLang(lang) {
	const prevLang = getLang();

	if(prevLang == lang)
		return;

	if(lang)
		localStorage.language = lang;
	else
		delete localStorage.language;

	loadLang(false);
	updateDates();

	if(prevLang == "ic-IC")
		location.reload();
}
