from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.environ["PATH"] += "/Users/akisubra/Downloads/selenium/"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



driver.get("http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)

download_element = driver.find_element(By.ID,"downloadButton")
download_element.click()

WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,"progress-label"),
        "Complete!"
    )
)