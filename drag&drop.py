import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
url="https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)
browser.maximize_window()
source_element=browser.find_element(By.ID,"column-a")
denstin_element=browser.find_element(By.ID,"column-b")
action=ActionChains(browser)
action.drag_and_drop(source_element,denstin_element).perform()
time.sleep(5)
browser.quit()