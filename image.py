import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

 

driver=webdriver.Chrome()
"https://the-internet.herokuapp.com/broken_images"
driver.get("https://the-internet.herokuapp.com/broken_images")


images= driver.find_elements(By.TAG_NAME,'img')
broken_image=[]
for image in images:
    src=image.get_attribute('src')
    if src:
        response=requests.get(src)
        if response.status_code != 200:
            broken_image.append(src)
            print(broken_image)

