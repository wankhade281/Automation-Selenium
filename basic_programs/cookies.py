import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
# Capture all the cookies created by browser
cookies = driver.get_cookies()
print("Numbers of cookies created", len(cookies))
print(cookies)  # show numbers of cookies

# Adding new cookie to browser
cookie = {"name":"new added cookie","value": "121212"}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print("length of cookies after one added", len(cookies))
print(cookies)  # show numbers of cookies

# Deleting cookie
driver.delete_cookie('new added cookie')
time.sleep(3)
cookies = driver.get_cookies()
print("length of cookies after one deleted",len(cookies))  # show numbers of cookies

# Deleting all the cookies
driver.delete_all_cookies()
time.sleep(3)
cookies = driver.get_cookies()
print("length of cookies after all deleted",len(cookies))  # show numbers of cookies