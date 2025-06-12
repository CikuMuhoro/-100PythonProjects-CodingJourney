from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

# handle cookies
try:
    # Wait up to 5 seconds for the "Accept all" button to appear (if it does)
    accept_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'Accept all') or contains(text(), 'I agree')]"))
    )
    accept_button.click()
    print("Cookie popup accepted.")
except:
    print("No cookie popup appeared.")
