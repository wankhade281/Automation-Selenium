import unittest

from selenium import webdriver


class TestAssertion(unittest.TestCase):
    def setUp(self):  # This Function is executed before every test execution
        self.driver = webdriver.Chrome()

    def test_assertEquals(self):
        driver = self.driver
        driver.get("https://www.irctc.co.in/nget/profile/user-registration")
        self.assertEqual("IRCTC Next Generation eTicketing System", driver.title, msg="Web page title is not same")

    def test_assertNotEquals(self):
        driver = self.driver
        driver.get("https://www.irctc.co.in/nget/profile/user-registration")
        self.assertNotEqual("Generation eTicketing System", driver.title, msg="Web page title is Equal")

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is True")
        b = False
        self.assertFalse(b, "b is False")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
