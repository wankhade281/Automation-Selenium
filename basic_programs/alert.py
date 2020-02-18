import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")  # we have to use different website for pop-up window
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/div/label/button").click()
time.sleep(5)
driver.switch_to_alert().accept()  # To close alert window using ok Button
driver.switch_to_alert().dismiss()  # To close alert window using Cancel Button