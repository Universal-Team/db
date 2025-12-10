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
	description: {label: "Description", type: "string", required: true},
	author: {label: "Author's Name", type: "string", required: true},
	avatar: {label: "Author's Avatar", type: "image"},
	website: {label: "App's Website", type: "string"},
	// Required
	systems: {label: "Native Systems", type: "multiselect", required: true, values: ["3ds", "ds"], labels: ["3DS", "DS"]},
	categories: {label: "Categories", type: "multiselect", required: true, values: ["game", "emulator", "app", "utility", "save-tool", "firm", "luma3DS"], labels: ["Game", "Emulator", "App", "Utility", "Save Tool", "FIRM", "Luma3DS"]},
	image: {label: "Banner Image", type: "image"},
	icon: {label: "Icon", type: "image", required: true},
	// Common
	unique_ids: {label: "CIA Unique ID(s)", type: "array"},
	long_description: {label: "Long Description (Markdown)", type: "textarea"},
	download_filter: {label: "Download Filter (regex)", type: "string"},
	// Rare
	autogen_scripts: {label: "Auto-generate Scripts", type: "bool", default: true},
	script_message: {label: "Pre-install message", type: "string"},
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
			author: "name"
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
		let temp = json;
		mappings[key].split("/").forEach(r => temp = temp[r]);
		appSchema[key].default = temp;
	}

	return true;
}


async function fetchInfo() {
	clearError();
	if(git.provider != "none") {
		git.repo = document.getElementById("repo").value;

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
		input.addEventListener("change", event => {
			clearError();

			let id = event.target.id;
			appInfo[id] = event.target.value;

			if(item.type == "array")
				appInfo[id] = appInfo[id].split(",").map(r => r.trim());

			let reset = document.getElementById(id + "-reset");
			if(reset) {
				reset.disabled = appInfo[id] == appSchema[id].default;
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
			appInfo[id] = event.target.checked;

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
			let labelText = item.labels?.[i] ?? option;

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

		appInfo[key] = item.default ?? new types[item.type];

		if(item.hidden)
			continue;

		let inputGroup = document.createElement("div");
		inputGroup.classList.add("input-group");

		let label = document.createElement("label");
		label.classList.add("input-group-text");
		label.htmlFor = key;
		label.innerText = item.label ?? key;
		if(item.required)
			label.innerText += "*";
		inputGroup.appendChild(label);

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
}

async function exportJson() {
	clearError();

	let appExport = structuredClone(appInfo);

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
			return error(`Error: Required item '${schema.label ?? key}' is unset!`);

		if(schema.type == "image" && !blank) {
			let res = await fetch(item, {method: "HEAD"});
			if(res.status != 200)
				return error(`Error ${res.status}: Image '${schema.label ?? key}' is not a valid link!`);

			let contentType = res.headers.get("Content-Type");
			if(contentType.split("/")[0] != "image")
				return error(`Error: Image '${schema.label ?? key}' is not an image! (Content Type: ${contentType})`);
		}

		if(!schema.hidden && (appExport[key] == appSchema[key].default || blank))
			delete appExport[key];
	}

	let dataString = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appExport, null, "\t"));

	let a = document.createElement("a");
	a.href = dataString;
	a.download = appInfo.title + ".json";
	a.click()
}

setGit(document.getElementById("git").value);