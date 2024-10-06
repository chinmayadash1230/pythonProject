import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()
url="https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)
slider=browser.find_element(By.XPATH,"//input[@type='range']")
action=ActionChains(browser)
action.click_and_hold(slider).move_by_offset(100,0).release()
time.sleep(3)
browser.quit()