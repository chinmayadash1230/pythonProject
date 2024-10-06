from datetime import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#windows scrool method 0 to body hight
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
chekboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for chekbox in chekboxes:
    chekbox.send_keys(Keys.SPACE)
cheked_count =0
for chekbox in chekboxes:
    if chekbox.is_selected():
        cheked_count +=1
expected_chek_count = 7
if cheked_count == expected_chek_count:
    print("ok")
else:
    print("not")
driver.quit()





