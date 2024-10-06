from datetime import datetime, timedelta
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By








# Set the url and get the webpage
browser = webdriver.Firefox()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)
# cancel the popup message by click it
browser.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
# switch to the date picker frame
frameLo = browser.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")

browser.switch_to.frame(frameLo)

# click to the date picker box
browser.find_element(By.CSS_SELECTOR,"#datepicker").click()
# set a current date,time
current_date= datetime.now()
# set next date or set any date we want by changing the value of timedelta
next_date = current_date + timedelta(days=1)   # if days=1 then next day, if  days=-1 then previous day and if days=0 then current date
# set format of date
formated_date = next_date.strftime("%m/%d/%Y")
# enter the date we want by send_Keys
browser.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formated_date + Keys.TAB)
sleep(3)
browser.quit()