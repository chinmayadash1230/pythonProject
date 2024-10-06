from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Firefox()

driver.maximize_window()
#creating key pair for id & passwrd
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/v1/"
driver .get(login_url)
#user box attribute and value
username_field = driver.find_element(By.ID,"user-name")
password_field = driver.find_element(By.ID,"password")
# automatic field the value using .send key
username_field.send_keys(username)
password_field.send_keys(password)
login_button =driver.find_element(By.ID,"login-button")
#login button disabled achi na nahi
assert not login_button.get_attribute("disabled")
login_button.click()
#login pare jou 2nd pa*ge kholiba tara attribute neli
succes = driver.find_element(By.CSS_SELECTOR,".product_label")
#succes  variable ra text format jouta front re asuchi taku call karibaku .text
assert succes.text== "Products"








