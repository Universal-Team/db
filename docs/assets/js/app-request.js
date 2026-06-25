const ISSUE_URL = "https://github.com/Universal-Team/db/issues/new?template=app-request.yml&title=";
const GITHUB_API = "api.github.com";
const GITLAB_BASE = "gitlab.com";
const CODEBERG_BASE = "codeberg.org";

let hasExported = false;

let git = {
	provider: null,
	repo: null,
	host: null,
};

let defaults = {
	string: "",
	textarea: "",
	image: "",
	array: Array,
	multiselect: Array,
	radio: "",
	bool: false,
};

let defaultHosts = {
	"github": GITHUB_API,
	"gitlab": GITLAB_BASE,
	"forgejo": CODEBERG_BASE
}

let appInfo = {};
let appSchema = {
	// Autofill
	github: {type: "string", hidden: true},
	gitlab: {type: "string", hidden: true},
	gitlab_host: {type: "string", hidden: true},
	forgejo: {type: "string", hidden: true},
	forgejo_host: {type: "string", hidden: true},
	title: {label: "App Title", type: "string", required: true},
	description: {label: "Description", type: "string", maxLength: 256, required: true},
	author: {label: "Author's Name", type: "string", required: true},
	avatar: {label: "Author's Avatar", type: "image"},
	// Required
	systems: {label: "Native Systems", type: "multiselect", required: true, values: ["3DS", "DS"], labels: ["3DS", "DS"]},
	categories: {label: "Categories", type: "multiselect", required: true, values: ["game", "emulator", "app", "utility", "plugin", "firm", "exploit", "media", "save-tool"], labels: ["Game", "Emulator", "App", "Utility", "Plugin", "FIRM", "Exploit", "Multimedia", "Save Tool"]},
	llm_generation: {label: "LLM Generated Content", type: "radio", required: true, values: ["yes", "minor", "no"], labels: ["Yes", "Minor (see guidelines!)", "No"], help: "If you have directly included the output of an LLM in any form in your work, then this should be 'yes'. This includes code, art, music, documentation, etc.\n\nIf you would like to self declare 'minor' LLM genertion, please make sure to check see the definition in the contribution guidelines linked above.\n\nLLM assistance (code analysis and review, debugging, etc) does not necessarily count as LLM generated content as long as the output is not directly incorporated into the work."},
	icon: {label: "Icon", help: "Preferably 48x48 or 32x32. The icon is not technically necessary, avatar will be used as a fallback, but I didn't want people to skip it. Copy the avatar URL if you don't have an icon.", type: "image", required: true},
	image: {label: "Banner Image", help: "Preferably a 3DS banner (256x128). Displayed on the Universal-DB website.", type: "image"},
	// Common
	unique_ids: {
		label: "CIA Unique ID(s)",
		help: 'The "UniqueId" in an RSF file. If you do not have a 3DS CIA build then skip this. Comma separated for multiple.',
		type: "array",
		validate: str => {
			let items = str.split(",").map(r => r.trim());
			let output = [];
			for(let item of items) {
				if(/^(\d+|0x[\da-fA-F]+)$/.test(item)) {
					let val = parseInt(item);
					if(val <= 0xFFFFF && val >= 0)
						output.push(val);
				}
			}

			return {status: !!output.length, value: output};
		}
	},
	long_description: {label: "Long Description (Markdown)", help: "This is displayed on the Unviersal-DB website.", type: "textarea"},
	website: {label: "App's Website", type: "string"},
	wiki: {label: "App's Wiki", help: "If left blank this will be autofilled with the GitHub Wiki, I just haven't implemented the check for that into this form.", type: "string"},
	license: {label: "License", help: "If this autofilled please do not change it, this exists for Forgejo.\n\nThis is the short form of the license ideally matching the GitHub API.\n\nEx: 'gpl-3.0', 'mit', 'cc0-1.0'.", type: "string"},
	license_name: {label: "License Name", help: "If this autofilled please do not change it, this exists for Forgejo.\n\nThe long form of the license name, ideally matching the GitHub API.\n\nEx: 'GNU General Public License v3.0', 'MIT License', 'Creative Commons Zero v1.0 Universal'.", type: "string"},
	download_filter: {label: "Download Filter (regex)", help: "File whitelist in case your app has files not caught by the blacklist. Most common of cross-platform apps.", type: "string"},
	// Rare
	autogen_scripts: {label: "Auto-generate Scripts", type: "bool", default: true},
	script_message: {label: "Pre-install message", help: "The confirmation message to display in Universal-Updater before installing. Leave blank for most apps.", type: "string"},
};

let apiMappings = {
	github: {
		repoApi: "/repos/",
		userApi: "/users/",
		repo: {
			github: "full_name",
			avatar: "owner/avatar_url",
			title: "name",
			description: "description",
			website: "html_url",
			license: "license/key",
			license_name: "license/name"
		},
		user: {
			author: "name?login"
		}
	},
	gitlab: {
		repoApi: `/api/v4/projects/`,
		repo: {
			gitlab: "path_with_namespace",
			avatar: "namespace/avatar_url",
			author: "namespace/name",
			title: "name",
			description: "description",
			icon: "avatar_url",
			website: "web_url",
			license: "license/key",
			license_name: "license/name"
		}
	},
	forgejo: {
		repoApi: `/api/v1/repos/`,
		repo: {
			forgejo: "full_name",
			avatar: "owner/avatar_url",
			author: "owner/full_name?owner/login",
			title: "name",
			description: "description",
			icon: "avatar_url",
			website: "website"
		}
	}
};

function clearError() {
	let errorDiv = document.getElementById("errorDiv");
	errorDiv.classList.remove("alert", "alert-danger");
	errorDiv.innerText = "";
}

function error(errorMessage) {
	let errorDiv = document.getElementById("errorDiv");
	errorDiv.classList.add("alert", "alert-danger");
	errorDiv.innerText = errorMessage;
	errorDiv.scrollIntoView();
}

function getSlug(str) {
	// strip accents
	str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "")

	// to lowercase and turn all non-latin letters/numbers to -
	return str.toLowerCase().replace(/[^\w-_]/g, "-");
}

function setGit(provider, host) {
	document.getElementById("git").value = provider;
	git.provider = provider;

	let gitDiv = document.getElementById("gitData");
	gitDiv.innerHTML = "";

	if(git.provider != "none") {
		git.host = host ? host : defaultHosts[git.provider];

		let div = document.createElement("div");
		div.classList.add("input-group");
		gitDiv.appendChild(div);

		let label = document.createElement("label");
		label.classList.add("input-group-text");
		label.htmlFor = "repo";
		label.innerText = "Repository";
		div.appendChild(label);

		let input = document.createElement("input");
		input.classList.add("form-control");
		input.name = "repo";
		input.id = "repo";
		input.value = git.repo;
		input.addEventListener("change", event => {
			git.repo = event.target.value;
			let value = git.repo.match(/(?:https:\/\/((github|gitlab|codeberg|gitea)\.(?:com|org))\/)?([\w._-]+\/[\w._-]+)/);
			if(git.repo != value[3]) {
				git.repo = value[3];
				document.getElementById("repo").value = git.repo;

				if(value[1]) {
					setGit(value[2].replace(/codeberg|gitea/, "forgejo"), value[1]);
				}
			}
		});
		div.appendChild(input);

		if(git.provider != "github") {
			let div = document.createElement("div");
			div.classList.add("input-group");
			gitDiv.appendChild(div);

			let label = document.createElement("label");
			label.classList.add("input-group-text");
			label.htmlFor = "host";
			label.innerText = "Host";
			div.appendChild(label);

			let input = document.createElement("input");
			input.classList.add("form-control");
			input.name = "host";
			input.id = "host";
			input.value = git.host;
			input.addEventListener("change", event => git.host = event.target.value);
			div.appendChild(input);
		}
	}
}

async function fetchApi(url, mappings) {
	let res;
	try {
		res = await fetch(url);
		if(res.status != 200) {
			error(`Error ${res.status}: Git repository not found`);
			return false;
		}
	} catch(e) {
		error(e);
		return;
	}

	let json = await res.json();
	for(let key in mappings) {
		let temp;
		let maps = mappings[key].split("?");
		for(let map of maps) {
			temp = json;
			map.split("/").forEach(r => temp = temp ? temp[r] : null);
			if(temp)
				break;
		}

		appSchema[key].default = temp;
	}

	return true;
}


async function fetchInfo() {
	clearError();

	hasExported = false;
	for(let item in appSchema)
		appSchema[item].default = null;

	if(git.provider != "none") {
		if(!git.repo)
			return error("Repository not set!");

		let apiRepo = git.provider == "gitlab" ? (encodeURIComponent(git.repo) + "?license=yes") : git.repo;
		let res = await fetchApi("https://" + git.host + apiMappings[git.provider].repoApi + apiRepo, apiMappings[git.provider].repo);
		if(!res)
			return;

		if(git.provider == "gitlab") {
			appSchema.avatar.default = "https://" + git.host + appSchema.avatar.default;

			if(git.host != GITLAB_BASE)
				appSchema.gitlab_host.default = git.host;
		}

		if(git.provider == "forgejo")
			appSchema.forgejo_host.default = git.host;

		if(git.provider == "github") {
			res = await fetchApi("https://" + git.host + apiMappings[git.provider].userApi + git.repo.split("/")[0], apiMappings[git.provider].user);
			if(!res)
				return;
		}
	}

	fillInfo();
}

function createInput(item, key) {
	if(["string", "textarea", "image", "array"].includes(item.type)) {
		let input = document.createElement(item.type == "textarea" ? "textarea" : "input");
		input.classList.add("form-control");
		input.id = key;
		input.type = "text";
		input.value = appInfo[key];
		input.required = item.required;
		if(item.maxLength)
			input.maxLength = item.maxLength;
		input.addEventListener("change", event => {
			clearError();

			let id = event.target.id;
			if(appSchema[id].validate) {
				let res = item.validate(event.target.value);
				if(res.status) {
					appInfo[id] = res.value;
					event.target.value = item.type == "array" ? res.value.join(", ") : res.value;
				}
			} else {
				appInfo[id] = event.target.value;

				if(item.type == "array")
					appInfo[id] = appInfo[id].split(",").map(r => r.trim());
			}

			let reset = document.getElementById(id + "-reset");
			if(reset) {
				reset.disabled = appInfo[id] == appSchema[id].default;
			}

			if(id == "title") {
				document.getElementById("submit-btn").href = ISSUE_URL + encodeURIComponent(appInfo.title);
			}
		});

		return [input];
	} else if(item.type == "bool") {
		let input = document.createElement("input");
		input.classList.add("form-check-input");
		input.id = key;
		input.type = "checkbox";
		input.checked = appInfo[key];
		input.required = item.required;
		input.addEventListener("change", event => {
			clearError();

			let id = event.target.id;
			if(appSchema[id].validate) {
				let res = appSchema[id].validate(event.target.checked);
				if(res.status) {
					appInfo[id] = res.value;
					event.target.checked = res.value;
				}
			} else {
				appInfo[id] = event.target.checked;
			}

			let reset = document.getElementById(id + "-reset");
			if(reset) {
				reset.disabled = appInfo[id] == appSchema[id].default;
			}
		});

		let div = document.createElement("div");
		div.classList.add("form-control");
		div.appendChild(input);
		return [div];
	} else if(item.type == "multiselect" || item.type == "radio") {
		let elements = [];
		let isRadio = item.type != "multiselect";

		for(let i in item.values) {
			let option = item.values[i];
			let labelText = item.labels ? item.labels[i] : option;

			let label = document.createElement("label");
			label.classList.add("btn", "btn-secondary", "flex-fill");
			label.htmlFor = `${key}-${option}`;
			label.innerText = labelText;

			let input = document.createElement("input");
			input.classList.add("btn-check");
			input.id = `${key}-${option}`;
			if(isRadio) input.name = key;
			input.type = isRadio ? "radio" : "checkbox";
			input.required = item.required;

			if(item.default == option && !item.disableAutofill) {
				input.checked = true;
			}

			if(isRadio) {
				input.addEventListener("change", event => {
					clearError();
					let [id, value] = event.target.id.split("-");
					appInfo[id] = value;

					let reset = document.getElementById(id + "-reset");
					if(reset) {
						reset.disabled = appInfo[id] == appSchema[id].default;
					}
				});
			} else {
				input.addEventListener("change", event => {
					clearError();

					let [_, id, value] = event.target.id.match(/(\w+)-(.+)/);
					if(appInfo[id].includes(value)) {
						appInfo[id].splice(appInfo[id].indexOf(value), 1);
					} else {
						appInfo[id].push(value);
					}
				});
			}

			elements.push(input);
			elements.push(label);
		}
		return elements;
	}
}

function fillInfo() {
	let div = document.getElementById("appData");
	div.innerHTML = "";
	appInfo = {};

	for(let key in appSchema) {
		let item = appSchema[key];

		appInfo[key] = (item.default && !item.disableAutofill) ? item.default : defaults[item.type];
		if(typeof appInfo[key] == "function")
			appInfo[key] = appInfo[key]();

		if(item.hidden)
			continue;

		let inputGroup = document.createElement("div");
		inputGroup.classList.add("input-group");

		let label = document.createElement("label");
		label.classList.add("input-group-text");
		label.htmlFor = key;
		label.innerText = item.label ? item.label : key;
		if(item.required)
			label.innerText += "*";
		inputGroup.appendChild(label);

		if(item.help) {
			let help = document.createElement("input");
			help.type = "button";
			help.classList.add("input-group-text");
			help.value = "(?)";
			help.addEventListener("click", () => { alert(item.help); });
			inputGroup.appendChild(help);
		}

		createInput(item, key).forEach(r => inputGroup.appendChild(r));

		if (appSchema[key].default && !appSchema[key].disableAutofill) {
			let reset = document.createElement("input");
			reset.classList.add("btn", "btn-outline-secondary");
			reset.type = "button";
			reset.value = "Reset";
			reset.htmlFor = key;
			reset.id = key + "-reset";
			reset.disabled = true;
			reset.addEventListener("click", event => {
				let id = event.target.htmlFor;
				if(appSchema[id].type == "bool") {
					document.getElementById(id).checked = appSchema[id].default;
				} else if(appSchema[id].type == "radio") {
					document.getElementById(`${id}-${appSchema[id].default}`).checked = true;
				} else {
					document.getElementById(id).value = appSchema[id].default;
				}
				appInfo[id] = appSchema[id].default;
				event.target.disabled = true;
			});

			inputGroup.appendChild(reset);
		}

		// div.appendChild(document.createElement("br"));
		div.append(inputGroup);
	}

	let download = document.createElement("input");
	download.classList.add("btn", "btn-primary");
	download.type = "button";
	download.value = "Export";
	download.addEventListener("click", exportJson);
	div.appendChild(download);

	let submit = document.createElement("a");
	submit.id = "submit-btn";
	submit.classList.add("btn", "btn-secondary", "ms-2");
	submit.innerText = "Submit";
	submit.href = ISSUE_URL + encodeURIComponent(appInfo.title);
	submit.addEventListener("click", event => {
		if(!hasExported) {
			event.preventDefault();
			error("You must export before submitting.");
		}
	});

	div.appendChild(submit);
}

async function exportJson() {
	clearError();

	hasExported = true;

	let clone = typeof structuredClone !== "undefined" ? structuredClone : obj => JSON.parse(JSON.stringify(obj));
	let appExport = clone(appInfo);

	for(let key in appExport) {
		let schema = appSchema[key];
		let item = appExport[key];
		let blank = true;
		switch(schema.type) {
			case "string":
			case "textarea":
			case "image":
			case "radio":
				blank = item === "";
				break;
			case "array":
			case "multiselect":
				blank = item.length == 0;
				break;
			case "bool":
				blank = false;
				break;
			default:
				break;
		}

		if(schema.required && blank)
			return error(`Error: Required item '${schema.label ? schema.label : key}' is unset!`);

		if(schema.type == "image" && !blank) {
			try {
				let res = await fetch(item, {method: "HEAD"});
				if(res.status != 200)
					return error(`Error ${res.status}: Image '${schema.label ? schema.label : key}' is not a valid link!`);

				let contentType = res.headers.get("Content-Type");
				if(contentType.split("/")[0] != "image")
					return error(`Error: Image '${schema.label ? schema.label : key}' is not an image! (Content Type: ${contentType})`);
			} catch(err) {
				let safeUrl = git.host == "github.com" ? "raw.githubusercontent.com" : git.host
				if(git.host == "github.com" || !item.startsWith("https://" + git.host))
					return error("Error: Failed to fetch image, make sure you're using " + safeUrl);
			}
		}

		if(blank || (!schema.hidden && appExport[key] == appSchema[key].default))
			delete appExport[key];
	}

	if(appExport.icon == appInfo.avatar)
		delete appExport.icon;

	let dataString = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appExport, null, "\t"));

	let a = document.createElement("a");
	a.href = dataString;
	a.download = getSlug(appInfo.title).replace(/-+/g, "-").replace(/^-|-$/g, "") + ".json";
	a.click()
}

setGit(document.getElementById("git").value);
