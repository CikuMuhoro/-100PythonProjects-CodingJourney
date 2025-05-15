import requests
from bs4 import BeautifulSoup
from pprint import pprint


def all_page_quotes():
    # open the page and request for data
    url = "http://quotes.toscrape.com"
    all_page_quotes = []

    # Extractint allquotes from all next pages
    while url:
        response = requests.get(url)

        # check if request is accesible
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            for quote_block in soup.find_all("div", class_="quote"):
                quote_text = quote_block.find("span", class_="text").text
                author = quote_block.find("small", class_="author").text
                tags = [
                    tag.text for tag in quote_block.find_all("a", class_="tag")]

                quote_data = {
                    "quote": quote_text,
                    "author": author,
                    "tags": tags
                }
                all_page_quotes.append(quote_data)

            # check for next page quotes
            next_btn = soup.find("li", class_="next")
            if next_btn:
                next_page_url = next_btn.find("a")["href"]
                url = "http://quotes.toscrape.com" + next_page_url
            else:
                url = None

        else:
            print("access denied")

    pprint(all_page_quotes)


all_page_quotes()
