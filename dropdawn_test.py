

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dropdown")
drop_down = driver.find_element(By.ID, "dropdown")
select = Select(drop_down)
#select.select_by_index(2)
#select.select_by_value("1")
#select.select_by_visible_text("Option 1")
target_value ="Option 2"
select = Select(drop_down)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is{target_value}")
        break
else:
    print(f"option '{target_value}' not found")


