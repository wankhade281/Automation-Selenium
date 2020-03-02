from selenium import webdriver
import unittest


class Test1Demo(unittest.TestCase):
    def setUp(self):  # This Function is executed before every test execution
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities={"browserName":"chrome",})

    def test_demo1(self):
        driver = self.driver
        driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
