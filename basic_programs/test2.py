import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://fundoopush-dev.bridgelabz.com/login')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("mat-input-0").send_keys("chetanwankhade281@gmail.com")
driver.find_element_by_id("mat-input-1").send_keys("chetan1234")
driver.find_element_by_class_name("mat-button-wrapper").click()
time.sleep(10)
driver.find_element_by_class_name("plus-div").click()
driver.find_element_by_xpath("//button[contains(text(),'ADD ARTICLE')]").click()
time.sleep(10)
#driver.find_element_by_xpath("//div[@class='quill-style']").click()
# driver.switch_to().alert().accept()
driver.find_element_by_xpath("//div[@class='quill-style']").send_keys("/home/admin1/Downloads/download.jpeg")
time.sleep(10)