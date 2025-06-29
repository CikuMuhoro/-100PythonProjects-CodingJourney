from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://duckduckgo.com/")

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
input("Press Enter AFTER solving CAPTCHA (if any) and cookie popup...\n")
time.sleep(5)

#scroll to load more result
for i in range (5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
#find all result container
results = driver.find_elements(By.CSS_SELECTOR, "[data-testid='result']")   

#Extract title link and snipet from the conainers
for container in results:
    try:
        title=container.find_element(By.CSS_SELECTOR, "[data-testid='result-title-a'] span")
        link=container.find_element(By.CSS_SELECTOR, "[data-testid='result-title-a']").get_attribute("href")
        snippet=container.find_element(By.CSS_SELECTOR, "[data-result ='snippet'] span").text
        
        print("Title : ", title.text)
        print("Link : ", link)
        print("Snippet : ", snippet)
        print("_"*60)
        
    except Exception as e:
        #skip if some part is mising
        continue
    
#close the driver
driver.quit(
        
    )
         
