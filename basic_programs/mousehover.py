from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.apprenticeship.gov.in/pages/Apprenticeship/home.aspx?AspxAutoDetectCookieSupport=1")
driver.maximize_window()
driver.implicitly_wait(2)
establish = driver.find_element_by_xpath("//*[@id='mnuMain']/ul/li[2]/a")
apprentices = driver.find_element_by_xpath("//*[@id='mnuMain']/ul/li[3]/a")
BTP = driver.find_element_by_xpath("//*[@id='mnuMain']/ul/li[4]/a")
verification = driver.find_element_by_xpath("//*[@id='mnuMain']/ul/li[5]/a")
TPA = driver.find_element_by_xpath("//*[@id='mnuMain']/ul/li[6]/a")
app_act = driver.find_element_by_xpath("//*[@id='mnuMain']/ul/li[7]/a")
goto = driver.find_element_by_xpath("//*[@id='mnuMain:submenu:30']/li[2]/a")

actions = ActionChains(driver)
actions.move_to_element(establish).move_to_element(apprentices).move_to_element(BTP).move_to_element(verification).move_to_element(TPA).move_to_element(app_act).move_to_element(goto).click().perform()