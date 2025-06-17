from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

# handle cookies
try:
    # Wait up to 10 seconds for the "Accept all" button to appear (if it does)
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'Accept all') or contains(text(), 'I agree')]"))
    )
    accept_button.click()
    print("Cookie popup accepted.")
except TimeoutException:
    print("No cookie popup appeared.")

    # wait for search bar and type in
search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q")))

# TYPE IN THE SERCH BAR AND SUBMIT
search_box.send_keys("learn selenium python" + Keys.ENTER)
