from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Set up ChromeDriver
service = Service("chromedriver.exe")  # Use "chromedriver" on Mac/Linux
driver = webdriver.Chrome(service=service)

# Open a simple website
driver.get("https://example.com")

# Wait for 5 seconds so we can see it
time.sleep(5)

# Close the browser
driver.quit()
