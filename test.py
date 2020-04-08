import requests

page = requests.get("https://heise.de").text

entry = str(len(page)) + "\n"

with open("file.db", "a") as f:
	f.write(entry)