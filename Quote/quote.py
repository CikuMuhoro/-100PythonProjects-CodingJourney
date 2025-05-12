import requests
from bs4 import BeautifulSoup

# request for the page
url = "http://quotes.toscrape.com"
responce = requests.get(url)

# check if the request is sucessful
if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, "html.parser")
else:
    print("failed to retrieve the page")

# Extract one quote
quote_block = soup.find("div", class_="quote")

quote_text = quote_block.find("span", class_="text").text
author = quote_block.find("small", class_="author").text
tag = tags = [tag.text for tag in quote_block.find_all("a", class_="tag")]

print("Quote: ", quote_text)
print("Author: ", author)
print("Tag: ", tags)
