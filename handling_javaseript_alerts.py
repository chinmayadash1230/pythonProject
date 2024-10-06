from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()

browser.get("https://the-internet.herokuapp.com/")
browser.maximize_window()
browser.execute_script("window.scrollTo(0, 500);")
browser.find_element(By.XPATH,"//a[normalize-space()='JavaScript Alerts']").click()
alert_bottem=browser.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']").click()
alert=browser.switch_to.alert
alert_text=alert.text
print(alert_text)
alert.accept()
