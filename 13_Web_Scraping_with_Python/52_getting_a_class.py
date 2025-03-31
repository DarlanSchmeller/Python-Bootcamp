import requests
import bs4

# Using Requests we grab the full content of the webpage using Requests, afterwards we parse it and create a soup/list object out of it using the BeautifulSoup library
res = requests.get("https://pt.wikipedia.org/wiki/Jonas_Salk")
soup = bs4.BeautifulSoup(res.text,'lxml')

search_class = soup.select("h2")
print(search_class)
print(search_class[2].text)

print('------------------------------------------')

search_class = soup.select("#Biografia")[0]
print(search_class.text)

print('------------------------------------------')

for item in soup.select("h2"):
    print(item.text)
