from selenium import webdriver
import time

# startchrome
driver = webdriver.Chrome()

# go to test website
driver.get("https://www.google.com/")

# set seconds to be up then quit
time.sleep(3)

# get the page html
html_code = driver.page_source

# print it
print(html_code)

driver.quit()
