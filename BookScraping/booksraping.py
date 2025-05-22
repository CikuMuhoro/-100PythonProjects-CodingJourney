import requests
from bs4 import BeautifulSoup


class Scraping_Book_listing:
    def __init__(self, ):
        self.books_details = []

    def book_scraping(self):
        for page in range(1, 6):
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"

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
                        "Title": title,
                        "Price": price,
                        "Rating": rating
                    }

                    self.books_details.append(books_data)

            else:
                print("failed to retrieve the page")

        for book in self.books_details:
            print(f"Title: {book['Title']}")
            print(f"Price: {book['Price']}")
            print(f"Rating: {book['Rating']}")
            print("-" * 30)


book = Scraping_Book_listing()
book.book_scraping()
