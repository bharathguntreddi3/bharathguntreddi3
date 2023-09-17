import random
import json
import requests
import os

limit=1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)

# API key to fetch quote or fact
response = requests.get(api_url, headers={'X-Api-Key': 'P9nis6bPQQRNLyrFK/yPaw==VJczzEp4moLZHGrk'})

if response.status_code == requests.codes.ok:
	fact = response.text
else:
	print("Error:", response.status_code, response.text)


# Reading the readme file
with open("README.md", mode="r", encoding="utf8") as f:
	readmeText = f.read()

# place to insert the fact
openingTag = "<h3 quote"
closingTag = "</h3 quote"

startIndex = readmeText.index(openingTag)
endIndex = readmeText.index(closingTag)

factMarkdown = "<h3 quote align='center'>" + fact + "." + "</h3 quote>"

content = readmeText[startIndex +
					len(openingTag): endIndex]
newContent = (
	readmeText[:startIndex]
	+ factMarkdown
	+ readmeText[endIndex + len(closingTag) + 1:]
)

# write again the new fact to the readme file
readme_file = open("README.md",
				mode="w", encoding="utf8")
readme_file.write(newContent)
