import time


from selenium import webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Firefox()
browser.get('https://www.selenium.dev/')
time.sleep(2)
browser.switch_to.new_window()
browser.get('https://playwright.dev')
time.sleep
number_window = len(browser.window_handles)
print(number_window)
tab_value=browser.window_handles
print(tab_value)
current_tab=browser
print(current_tab)

browser.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()
First_tab=browser.window_handles[0]
if current_tab !=First_tab:
    browser.switch_to.window(First_tab)
    browser.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()
    

