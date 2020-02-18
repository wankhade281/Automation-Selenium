import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i").click()
time.sleep(2)
# scroll down the page up to given element
flag = driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[15]/a/label/strong")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[12]/label").click()
time.sleep(2)
print("/n current window handle==> ==> ==>111",driver.current_window_handle)
flag = driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[12]/ul/li[6]/a")
driver.execute_script("arguments[0].scrollIntoView();",flag)
print("current url is--> --> --> --> -->",driver.current_url)
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i")
driver.find_element(By.LINK_TEXT, "Link Your Aadhaar").click()
window_after = driver.window_handles[1]  # To switch to the newly open window
driver.switch_to_window(window_after)  #
print("current url is--> --> --> --> -->",driver.current_url)
driver.implicitly_wait(20)
driver.find_element_by_id("download").click()
