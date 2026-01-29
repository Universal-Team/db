const ISSUE_URL = "https://github.com/Universal-Team/db/issues/new?template=app-request.yml&title=";
const GITHUB_API = "https://api.github.com";
const GITLAB_BASE = "https://gitlab.com";
const GITLAB_API = `${GITLAB_BASE}/api/v4`;

let git = {
	provider: null,
	repo: null,
};

let types = {
	string: String,
	textarea: String,
	image: String,
	array: Array,
	multiselect: Array,
	bool: Boolean,
};

let appInfo = {};
let appSchema = {
	// Autofill
	github: {type: "string", hidden: true},
	gitlab: {type: "string", hidden: true},
	title: {label: "App Title", type: "string", required: true},
	description: {label: "Description", type: "string", maxLength: 256, required: true},
	author: {label: "Author's Name", type: "string", required: true},
	avatar: {label: "Author's Avatar", type: "image"},
	// Required
	systems: {label: "Native Systems", type: "multiselect", required: true, values: ["3DS", "DS"], labels: ["3DS", "DS"]},
	categories: {label: "Categories", type: "multiselect", required: true, values: ["game", "emulator", "exploit", "app", "utility", "save-tool", "firm"], labels: ["Game", "Emulator", "Exploit", "App", "Utility", "Save Tool", "FIRM"]},
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
	}},
	long_description: {label: "Long Description (Markdown)", help: "This is displayed on the Unviersal-DB website.", type: "textarea"},
	website: {label: "App's Website", type: "string"},
	wiki: {label: "App's Wiki", help: "If left blank this will be autofilled with the GitHub Wiki, I just haven't implemented the check for that into this form.", type: "string"},
	download_filter: {label: "Download Filter (regex)", help: "File whitelist in case your app has files not caught by the blacklist. Most common of cross-platform apps.", type: "string"},
	// Rare
	autogen_scripts: {label: "Auto-generate Scripts", type: "bool", default: true},
	script_message: {label: "Pre-install message", help: "The confirmation message to display in Universal-Updater before installing. Leave blank for most apps.", type: "string"},
};

let apiMappings = {
	github: {
		repoApi: `${GITHUB_API}/repos/`,
		userApi: `${GITHUB_API}/users/`,
		repo: {
			github: "full_name",
			avatar: "owner/avatar_url",
			title: "name",
			description: "description",
			website: "html_url"
		},
		user: {
			author: "name?login"
		}
	},
	gitlab: {
		repoApi: `${GITLAB_API}/projects/`,
		repo: {
			gitlab: "full_name",
			avatar: "namespace/avatar_url",
			author: "namespace/name",
			title: "name",
			description: "description",
			website: "web_url"
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

function setGit(provider) {
	git.provider = provider;

	let gitDiv = document.getElementById("gitData");
	gitDiv.innerHTML = "";

	if(git.provider != "none") {
		let label = document.createElement("label");
		label.classList.add("input-group-text");
		label.htmlFor = "repo";
		label.innerText = "Repository";

		let input = document.createElement("input");
		input.classList.add("form-control");
		input.name = "repo";
		input.id = "repo";

		gitDiv.appendChild(label);
		gitDiv.appendChild(input);
	}
}

async function fetchApi(url, mappings) {
	let res = await fetch(url);
	if(res.status != 200) {
		error(`Error ${res.status}: Git repository not found`);
		return false;
	}

	let json = await res.json();
	for(let key in mappings) {
		let temp;
		let maps = mappings[key].split("?");
		for(let map of maps) {
			temp = json;
			map.split("/").forEach(r => temp = temp[r]);
			if(temp)
				break;
		}

		appSchema[key].default = temp;
	}

	return true;
}


async function fetchInfo() {
	clearError();
	if(git.provider != "none") {
		git.repo = document.getElementById("repo").value;
		let value = git.repo.match(/(?:https:\/\/(github|gitlab).com\/)?([\w._-]+\/[\w._-]+)/);
		if(git.repo != value[2]) {
			git.repo = value[2];
			document.getElementById("repo").value = git.repo;

			if(value[1]) {
				git.provider = value[1];
				document.getElementById("git").value = git.provider;
			}
		}

		if(!git.repo)
			return error("Repository not set!");

		let apiRepo = git.provider == "gitlab" ? encodeURIComponent(git.repo) : git.repo;
		let res = await fetchApi(apiMappings[git.provider].repoApi + apiRepo, apiMappings[git.provider].repo);
		if(!res)
			return;

		if(git.provider == "gitlab")
			appSchema.avatar.default = GITLAB_BASE + appSchema.avatar.default;
	
		if(git.provider == "github") {
			res = await fetchApi(apiMappings[git.provider].userApi + git.repo.split("/")[0], apiMappings[git.provider].user);
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
				console.log(res)
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
				console.log(res)
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
	} else if(item.type == "multiselect") {
		let elements = [];

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
			input.type = "checkbox";
			input.required = item.required;
			input.addEventListener("change", event => {
				clearError();

				let [id, value] = event.target.id.split("-");
				if(appInfo[id].includes(value)) {
					appInfo[id].splice(appInfo[id].indexOf(value), 1);
				} else {
					appInfo[id].push(value);
				}
			});
			
			elements.push(input);
			elements.push(label);
		}
		return elements;
	}
}

function fillInfo() {
	let div = document.getElementById("appData");
	div.innerHTML = "";

	for(let key in appSchema) {
		let item = appSchema[key];

		appInfo[key] = item.default ? item.default : new types[item.type];

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
		
		if (appSchema[key].default) {
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
				} else {
					document.getElementById(id).value = appSchema[id].default;
				}
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
	div.appendChild(submit);
}

async function exportJson() {
	clearError();

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
				blank = item == "";
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
				return error("Error: Failed to fetch image, make sure you're using raw.githubusercontent.com");
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
