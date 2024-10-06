import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
url = "https://jqueryui.com/"
driver.get(url)
all_link =driver.find_elements(By.TAG_NAME,"a")
print(f"total no of link:{len(all_link)} link found in the page")

for link in all_link:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken link:{href} status_code:{response.status_code}")
driver.quit()