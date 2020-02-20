import time
import unittest
from selenium import webdriver


class FundooPush(unittest.TestCase):
    def setUp(self):  # This Function is executed before every test execution
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://fundoopush-dev.bridgelabz.com/login')

        driver.implicitly_wait(10)
        driver.find_element_by_id("mat-input-0").send_keys("chetanwankhade281@gmail.com")
        driver.find_element_by_id("mat-input-1").send_keys("chetan1234")
        driver.find_element_by_class_name("mat-button-wrapper").click()
        time.sleep(10)
        driver.find_element_by_class_name("plus-div").click()
        driver.find_element_by_xpath("//button[contains(text(),'ADD ARTICLE')]").click()
        time.sleep(10)
        filepath = "/home/admin1/Downloads/download.jpeg"
        test = driver.find_element_by_xpath("//img[@class='ng-tns-c1-1426 addImage ng-star-inserted opacity-class']")
        test.send_keys(filepath)

        time.sleep(20)
        # element.send_keys("/home/admin1/Downloads/download.jpeg")

    def tearDown(self):  # This function is executed after every test execution
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
# @unittest.skip("Due to the issue on site")
# @unittest.SkipTest
#     def test_search(self):
#         print('This is a Test Search')
