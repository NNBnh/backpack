const fs   = require("fs");
const yaml = require("js-yaml");


const backpack = yaml.load(fs.readFileSync("backpack.yaml", {encoding: "utf-8"}));


let packages = {
	"arch": [],
	"aur":  [],
	"pypi": [],
};

let repology = []

const available_repositories = ["arch", "aur", "pypi"]

for (const package of backpack["packages"]) {
	for (const [repository, name] of Object.entries(package)) {
		if(repository === "repology") {
			repology.push("https://repology.org//api/v1/project/" + name);
			break;
		} else if(available_repositories.indexOf(repository) >= 0) {
			packages[repository].push(name);
			break;
		}
	}
}

console.log(JSON.stringify(packages, null, 2));
