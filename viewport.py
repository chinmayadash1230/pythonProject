import time

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://web.whatsapp.com")
view =[(123,956),(456,985),(748,659),(987,236),(969,669)]
try:
    for width,height in view:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.quit()

