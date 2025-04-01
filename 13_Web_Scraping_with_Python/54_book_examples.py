# GOAL: Get the title of every book with a two star rating

import requests
import bs4

# In this case since there's pagination in place, the .format method is useful to insert dynamically the page we want to scrape
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

paginated_url = base_url.format(1)
print(paginated_url)

html_data = requests.get(paginated_url)
soup = bs4.BeautifulSoup(html_data.text,"lxml")
products = soup.select(".product_pod")
print(products)


# We can check if something is 2 stars (either through string call or example.select(rating))
# We can also do example.select('a')[1]['title'] to grab the book title
example = products[0]
print(example)
print(example.select(".star-rating.Three"))
print(example.select("a")[1]['title'])


two_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)