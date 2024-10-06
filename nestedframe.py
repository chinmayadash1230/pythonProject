from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()
url="https://the-internet.herokuapp.com/nested_frames"
browser.get(url)
browser.maximize_window()
#switching to the top frame
browser.switch_to.frame("frame-top")
#switching to the middle frame
browser.switch_to.frame("frame-middle")
content=browser.find_element(By.ID,"content").text
print("content in middle frame :",content)


#switch to difult content
browser.switch_to.default_content()
browser.switch_to.frame("frame-bottom")
content_bottem=browser.find_element(By.TAG_NAME,"body").text
print("content in content_bottem :  ",content_bottem)



