import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i").click()
# driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[2]/label/span").click()
# driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[2]/ul/li[4]/label/span[1]").click()


# ele = driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[2]/ul/li[4]/label/span[1]")
# drp = Select(ele)
# drp.select_by_visible_text("Group Booking")
# drp.select_by_value("IRCTC TRAINS")
# drp.select_by_index(1)


driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
# driver.find_element_by_xpath("//*[@id='divMain']/div/app-user-registration/div[2]/div/div[2]/div[4]/form/div[5]/div[2]/p-dropdown/div/div[3]/span").click()
ele = driver.find_element(By.TAG_NAME, "span")
drp = Select(ele)
drp.select_by_visible_text("What is your pet name?")