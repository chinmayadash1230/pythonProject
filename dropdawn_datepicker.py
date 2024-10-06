from datetime import datetime,timedelta


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from dropdawn_test import select

browser=webdriver.Firefox()
url="https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
browser.maximize_window()
browser.find_element(By.ID,"datepicker2").click()
current_date=datetime.now()
print(current_date)


next_day=current_date+ timedelta(days=1)
print(next_day)


Next_day=(str(next_day.day))
print(Next_day)
current_month=datetime.now().month
current_year=current_date.year

next_month=(current_month %12)+1
next_month_year = f"{next_month}/{current_year}"
month_dropdown = browser.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select = Select(month_dropdown)
select.select_by_value(str(next_month_year))



