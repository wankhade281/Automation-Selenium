import unittest

from selenium import webdriver


class TestParallel(unittest.TestCase):
    def setUp(self):  # This Function is executed before every test execution
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities={"browserName":"chrome",})

    def test_assertEquals(self):
        driver = self.driver
        driver.get("https://www.irctc.co.in/nget/profile/user-registration")

    def test_parallel(self):
        driver = self.driver
        driver.get("https://www.irctc.co.in/nget/profile/user-registration")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
