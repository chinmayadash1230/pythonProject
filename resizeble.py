from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains

browser=webdriver.Firefox()
url="https://demo.automationtesting.in/Resizable.html"
browser.get(url)
resizeble_element=browser.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
intial_element=browser.find_element(By.XPATH,"//div[@id='resizable']")
intial_size=intial_element.size
print(intial_size)

#action_chain = ActionChains(browser)

#action_chain.click_and_hold(resizeble_element).move_by_offset(100,100).release()
#resizeble_elemen=intial_element.size
#print(resizeble_elemen)