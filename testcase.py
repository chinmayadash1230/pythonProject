from matplotlib.pyplot import title
from selenium import webdriver
browser =webdriver.Firefox()
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
title = browser.title
print(title)
assert title == "OrangeHRM"