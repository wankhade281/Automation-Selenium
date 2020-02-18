import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")   # we have to use different website for Frames window
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/div/label/button").click()
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='google_ads_iframe_/37179215/GPT_NWEB_LOGIN_TOP_0__container__']"))
driver.switch_to.default_content()