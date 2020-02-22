from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
import time


class UsingWrappers1():

    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/profile/user-registration"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("userName")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='userName']", locatorType="xpath")
        textField2.clear()


ff = UsingWrappers1()
ff.test()
