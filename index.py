import random
import json
import requests
import os

# Getting API key from environment variable
API_KEY = os.environ.get('api_key')

# Getting a random quote from the API
category = ['inspirational','dreams',
			'experience',
			'success']
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category[random.randint(0,3)])
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

if response.status_code == requests.codes.ok:
	quote=response.text
	quotes = json.loads(quote)
	q=quotes[0]['quote']
	# In case of receiving multiple quotes, 
	# we will take the first one
	mainQuote=q.split('.')[0]
else:
	print("Error:", response.status_code, response.text)


# Reading the readme file
with open("README.md", mode="r", encoding="utf8") as f:
	readmeText = f.read()

# Finding the tag where the quote is to be replaced
openingTag = "<h3 quote"
closingTag = "</h3 quote"

startIndex = readmeText.index(openingTag)
endIndex = readmeText.index(closingTag)

quoteMarkdown = "<h3 quote align='center'>" + mainQuote + "." + "</h3 quote>"

content = readmeText[startIndex + len(openingTag) : endIndex]
newContent = (
	readmeText[:startIndex] + quoteMarkdown + readmeText[endIndex + len(closingTag) + 1 :]
)

# Writing new Quote into readme file
readme_file = open("README.md", mode="w", encoding="utf8")
readme_file.write(newContent)
