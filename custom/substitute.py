#!/usr/bin/python

colors = {}

with open("colors-waybar.css", "r") as wal_colors:
	for line in wal_colors.readlines():
		if line.startswith("@define-color "):
			line = line.replace("@define-color ", "").replace(";", "")
			name, color = line.split()
			colors[name] = color

produced = ""

with open("custom-template.css", "r") as template:
	for line in template.readlines():
		if "@" in line and "--" in line:
			name = line[line.find("@"):line.find(";")]
			line = line.replace(name, f"{colors[name[1:]]}ff")
		produced += line

with open("custom.css", "w") as custom:
	custom.write(produced)
