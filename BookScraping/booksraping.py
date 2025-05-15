import requests
from bs4 import BeautifulSoup


class Scraping_Book_listing:
    def __init__(self, titles=None, prices=None, rating=None):
        self.titles = titles
        self.prices = prices
        self.rating = rating

    def book_scraping(self):
        url = "https://books.toscrape.com/"
        books_details = []

        while url:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                for Every_book in soup.find_all("article", class_="product_pod"):
                    title = Every_book.h3.a["title"]
                    price = Every_book.find("p", class_="price_color").text
                    rating_class = Every_book.find(
                        "p", class_="star-rating")["class"]
                    rating = rating_class[1] if len(
                        rating_class) > 1 else "unknown"

                    books_data = {
                        "Title ": title,
                        "Price ": price,
                        "Rating ": rating
                    }

                    books_details.append(books_data)
                print(books_details)

        else:
            print("failed to retrieve the page")


book = Scraping_Book_listing(None, None, None)
book.book_scraping()
