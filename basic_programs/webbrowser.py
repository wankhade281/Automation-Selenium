from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox('/home/admin1/Downloads/geckodriver-v0.26.0-linux64')
driver.get("http://www.python.org")
print(driver.title)
print(driver.current_url)
print(driver.get_cookies())
print(driver.get_screenshot_as_png())
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
