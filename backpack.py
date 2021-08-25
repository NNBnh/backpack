#!/bin/python3

import yaml, requests, json, itertools, difflib, multiprocessing


def get_package(package):
	repology_datas = json.loads(
		requests.get("https://repology.org/api/v1/project/" + package).content
	)

	for available_repositorie in available_repositories:
		packages = [
			pick_packages(
				package,
				[
					repology_data["binname"]
					for repology_data in repology_datas
					if repology_data["repo"] == available_repositorie
					and repology_data["status"] == package_status
				],
			)
			for package_status in [
				"newest",
				"devel",
				"unique",
				"outdated",
				"noscheme",
				"untrusted",
				"ignored",
				"vulnerable",
				"incorrect",
				"rolling",
				"legacy",
			]
		]
		packages = list(filter(None, packages))
		packages = list(itertools.chain.from_iterable(packages))

		if packages:
			repository = available_repositorie

			break

	print(packages)
	add_package(packages[0], repository)


def pick_packages(name, names):
	if names:
		sorted_names = difflib.get_close_matches(name, names, n=len(names))

		return sorted_names + [
			unsorted_names
			for unsorted_names in names
			if unsorted_names not in sorted_names
		]


def add_package(package, repository):
	global packages_list

	if repository in packages_list:
		packages_list[repository] += [package]
	else:
		packages_list[repository] = [package]


with open("backpack.yaml", "rt") as file:
	backpack_data = yaml.safe_load(file)

available_repositories = ["arch", "aur", "pypi"]

packages_list = {}
for package in backpack_data["packages"]:
	for repository, name in package.items():
		add_package(name, repository)

# if "repology" in packages_list:
# 	multiprocessing.Pool().map(get_package, packages_list["repology"])


print(packages_list)
