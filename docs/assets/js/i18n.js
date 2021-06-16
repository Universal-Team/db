---
---

let i18n = {
	{%- for language in site.data.i18n -%}
		{%- for lang in site.data.languages -%}{%- if lang[1].id == language[0] -%}
			"{{ language[0] }}": {
				"dir": "{{ lang[1].dir }}",
				"strings": {
					{%- for item in language[1] -%}
						"{{ item[0] | replace: '"', '\"' }}":"{{ item[1] | replace: '"', '\"' }}"{% unless forloop.last %},{% endunless %}
					{%- endfor -%}
				}
			},
		{%- endif -%}{%- endfor -%}
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
	if(document.dir == "rtl") {
		document.getElementById("bootstrap-stylesheet").integrity = "sha384-mUkCBeyHPdg0tqB6JDd+65Gpw5h/l8DKcCTV2D2UpaMMFd7Jo8A+mDAosaWgFBPl";
		document.getElementById("bootstrap-stylesheet").href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.rtl.min.css";
	} else {
		document.getElementById("bootstrap-stylesheet").integrity = "sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1";
		document.getElementById("bootstrap-stylesheet").href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
	}

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
