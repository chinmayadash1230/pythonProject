import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")
iframe= driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)
text_Editor =driver.find_element(By.ID,"tinymce")
#text_Editor.clear()
text_Editor.send_keys("chinmaya dash automation tester")
time.sleep(5)
driver.switch_to.default_content()
out_sidelink=driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']").click()
driver.quit()

