import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(2)
driver.save_screenshot("/home/admin1/Pictures/firstscreenshot.png")  # store into folder as png file
# driver.get_screenshot_as_file("/home/admin1/Pictures/firstscreenshot.jpg") 
