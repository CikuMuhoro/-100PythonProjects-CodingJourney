import requests
from bs4 import BeautifulSoup
from pprint import pprint


def same_page_quotes():
    # open the page and request for data
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    # check if request is accesible
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    else:
        print("access denied")

    # Extractint allquotes from first page
    first_page_quotes = []

    for quote_block in soup.find_all("div", class_="quote"):
        quote_text = quote_block.find("span", class_="text").text
        author = quote_block.find("small", class_="author").text
        tag = tags = [
            tag.text for tag in quote_block.find_all("a", class_="tag")]

        quote_data = {
            "quote": quote_text,
            "author": author,
            "tags": tags
        }
        first_page_quotes.append(quote_data)

    pprint(first_page_quotes)


same_page_quotes()
