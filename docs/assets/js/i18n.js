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

var strings = i18n["en-US"].strings;

const _jipt = [];

loadHead();

function loadHead(lang) {
	const languageID = lang || getLang();

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

		const langCheck = setInterval(function() {
			const jipt = document.getElementsByClassName("crowdin-jipt");
			if(jipt && jipt.length > 4) {
				clearInterval(langCheck);
				if(["he"].includes(jipt[4].contentWindow.document.getElementById("jipt-target-languages").value)) {
					document.dir = "rtl";
					const bootstrapStylesheet = document.getElementById("bootstrap-stylesheet");
					bootstrapStylesheet.integrity = "sha384-mUkCBeyHPdg0tqB6JDd+65Gpw5h/l8DKcCTV2D2UpaMMFd7Jo8A+mDAosaWgFBPl";
					bootstrapStylesheet.href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.rtl.min.css";
				}
			}
		}, 500);
		const script = document.createElement("script");
		script.src = "//cdn.crowdin.com/jipt/jipt.js";
		document.head.appendChild(script);
	}
}

function loadLang(initing) {
	const languageID = getLang();
	if(!languageID || (initing && languageID == "en-US"))
		return;

	if(!initing)
		loadHead(false, languageID);

	if(!(languageID in i18n))
		return console.warn("Language not found", languageID);

	strings = i18n[languageID].strings;

	const i18nElements = document.getElementsByClassName("i18n");
	for(i = 0; i < i18nElements.length; i++) {
		const element = i18nElements[i];
		for(j = 0; j < element.classList.length; j++) {
			const match = element.classList[j].match(/(innerHTML|title|placeholder|ariaLabel|value|data-(.*?))-(.*)/);
			if(match) {
				const str = strings[match[3]];
				if(str) {
					if(match[2])
						element.dataset[match[2]] = str.replace(/\${(.*)}/g, function(full, capture) { return element.dataset[capture]; });
					else
						element[match[1]] = str.replace(/\${(.*)}/g, function(full, capture) { return element.dataset[capture]; });
				} else {
					console.warn("Translation is missing string", match[3]);
				}
			}
		}
	}

	const dropdownLangs = document.getElementById("language-dropdown").children;
	for(i = 0; i < dropdownLangs.length; i++) {
		const element = dropdownLangs[i];
		if(element.children[0].dataset.lang == languageID) {
			element.children[0].classList.add("active");
		} else {
			element.children[0].classList.remove("active");
		}
	}

	document.getElementById("translate-on-crowdin").href = "https://" + (i18n[languageID].crowdin || "www") + ".crowdin.com/project/universal-db";
}

function getLang() {
	if(localStorage.language) {
		return localStorage.language;
	}

	const languages = window.navigator.languages || [window.navigator.language];
	for(i = 0; i < languages.length; i++) {
		const languageIds = Object.keys(i18n);
		for(j in languageIds) {
			if(languageIds[j] == languages[i].substr(0, 2) + "-" + languages[i].substr(3, 2).toUpperCase()) {
				return languageIds[j];
			}
		}

		// If no match for lang-COUNTRY, try just lang
		for(j in languageIds) {
			if(languageIds[j].substr(0, 2) == languages[i]) {
				return languageIds[j];
			}
		}
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
