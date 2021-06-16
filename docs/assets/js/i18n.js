---
---

let i18n = {
	{%- for language in site.data.i18n -%}
		"{{ language[0] }}": {
			"dir": {%- for lang in site.data.languages -%}{%- if lang[1].id == language[0] -%}"{{- lang[1].dir -}}"{%- endif -%}{%- endfor -%},
			"strings": {
				{%- for item in language[1] -%}
					"{{ item[0] | replace: '"', '\"' }}":"{{ item[1] | replace: '"', '\"' }}"{% unless forloop.last %},{% endunless %}
				{%- endfor -%}
			}
		}{% unless forloop.last %},{% endunless %}
	{%- endfor -%}
};

loadLang(true);

function loadLang(initing) {
	let languageID = getLang();

	if(!languageID || (initing && languageID == "en-US"))
		return;

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

	document.documentElement.lang = languageID;
	document.documentElement.dir = i18n[languageID].dir;

	for(let element of document.getElementById("language-dropdown").children) {
		if(element.children[0].lang == languageID) {
			element.children[0].classList.add("active");
		} else {
			element.children[0].classList.remove("active");
		}
	}
}

function getLang() {
	if(localStorage.language)
		return localStorage.language;

	for(let wl of window.navigator.languages) {
		let l = Object.keys(i18n).find(r => r.substr(0, 2) == wl.substr(0, 2));
		if(l)
			return languageID = `${l.substr(0, 2)}-${l.substr(3, 3).toUpperCase()}`;
	}
}

function setLang(lang) {
	if(getLang() == lang)
		return;

	if(lang)
		localStorage.language = lang;
	else
		delete localStorage.language;

	loadLang(false);
}
