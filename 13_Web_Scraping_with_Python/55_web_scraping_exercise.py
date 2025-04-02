
# TASK: Import any libraries you think you'll need to scrape a website.

import requests
import bs4


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TASK: Use requests library and BeautifulSoup to connect to https://quotes.toscrape.com/ and get the HMTL text from the homepage.

scraped_data = requests.get("https://quotes.toscrape.com/") 
html_data = bs4.BeautifulSoup(scraped_data.text,"lxml")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TASK: Get the names of all the authors on the first page.

authors = html_data.select('.author')
for author in authors:
    print(author.get_text())



print('\n')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TASK: Create a list of all the quotes on the first page.
quotes_list = []

quotes = html_data.select('.quote .text')

for quote in quotes:
    quotes_list.append(quote.get_text())

print(quotes_list)



print('\n')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.

tags = html_data.select(".tags-box .tag")

for tag in tags:
    print(tag.get_text())



print('\n')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

found_page_limit = False
count = 1
unique_authors_list = []

while not found_page_limit:
    formatted_url = f"http://quotes.toscrape.com/page/{count}/"
    scraped_data = requests.get(formatted_url)
    if scraped_data.status_code == 200:
        html_data = bs4.BeautifulSoup(scraped_data.text, "lxml")

        if html_data.find_all('div', class_='quote'):   # Checks if there is any quote found, if not, we didn't manage to scrape the page
            count += 1
            
            authors = html_data.select('.author')
            for author in authors:
                if author.get_text() not in unique_authors_list:
                    unique_authors_list.append(author.get_text())
        else:
            found_page_limit = True
    else:
        found_page_limit = True

for unique_author in unique_authors_list:
    print(unique_author)

    