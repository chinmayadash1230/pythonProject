import time

from selenium import webdriver

from selenium .webdriver.chrome.options import Options
chrome_option=Options()
chrome_option.add_argument("incognito")
driver=webdriver.Chrome(options=chrome_option)
driver.maximize_window()
time.sleep(3)
driver.get("https://www.google.com")
