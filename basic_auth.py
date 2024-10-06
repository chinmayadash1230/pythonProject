from selenium import webdriver
username='admin'
password='admin'

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#https://username:password@domain/path