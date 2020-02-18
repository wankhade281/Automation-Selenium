import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")   # we have to use different website for Frames window
driver.maximize_window()
time.sleep(3)
# scroll down the page by pixels
# driver.execute_script("window.scrollBy(0,1000)","")

# scroll down the page up to given element
# flag = driver.find_element_by_xpath("//*[@id='divMain']/div/app-main-page/div[11]/div/div[5]/div/div[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

# scroll down till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
