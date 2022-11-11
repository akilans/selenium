from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os

os.environ["PATH"] += "/Users/akisubra/Downloads/selenium"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(30)

sum1 = driver.find_element(By.ID,"sum1")
sum2 = driver.find_element(By.ID,"sum2")

sum1.send_keys(10)
sum2.send_keys(5)
btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()