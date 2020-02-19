import time
import unittest

from selenium import webdriver


class FundooPush(unittest.TestCase):
    def setUp(self):  # This Function is executed before every test execution
        self.driver = webdriver.Chrome()

    @unittest.SkipTest
    def test_search(self):
        print('This is a Test Search')

    @unittest.skip("Due to the issue on site")
    def test_login(self):
        driver = self.driver
        driver.get('https://fundoopush-dev.bridgelabz.com/login')
        driver.maximize_window()
        driver.find_element_by_id("mat-input-0").send_keys("chetanwankhade281@gmail.com")
        driver.find_element_by_id("mat-input-1").send_keys("chetan1234")
        driver.find_element_by_class_name("mat-button-wrapper").click()
        driver.find_element_by_tag_name("mat-icon").click()
        time.sleep(50)
        driver.find_element_by_xpath("//button[contains(text(),'ADD ARTICLE')]").click()
        time.sleep(50)

    def tearDown(self):  # This function is executed after every test execution
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
