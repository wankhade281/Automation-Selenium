from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
links = driver.find_elements(By.TAG_NAME, "a")     # To find number of links present in page
print("Number of links present in page", len(links))
for link in links:
    print(link.text)

# Two types to find link
# 1. link text
# 2. Partial link text

# How to click on the link
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i")
driver.find_element(By.LINK_TEXT, "FLIGHTS").click()
# driver.find_element(By.PARTIAL_LINK_TEXT)
