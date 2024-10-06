from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
url_name ="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url_name)
driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()

driver.maximize_window()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.back()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()




