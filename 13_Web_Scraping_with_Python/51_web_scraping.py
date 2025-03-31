# Requests allows us to send a request to whatever URL we want, this allows us to retrieve the HTML for the page

import requests

result = requests.get("http://www.example.com")

print(type(result))
print(result.text)

print('-------------------------------------------------------- \n')

# We can use BeautifulSoup (bs4) in order to parse the text retrieved

import bs4

soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup) # The soup object is much clearer to read, we can use it to get tags and other data

print('-------------------------------------------------------- \n')

# We can use the BeautifulSoup library to get specific data we want, it returns a list like soup object so we may manipulate it like one
print(soup.select('title')[0].getText())
print(soup.select('h1'))
site_paragraphs = soup.select('p')
print(site_paragraphs)