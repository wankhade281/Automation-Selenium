from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i").click()
element = driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[2]/label")
action = ActionChains(driver)
action.double_click(element).perform()  # Double click on element
