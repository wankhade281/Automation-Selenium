import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def test_browser_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.irctc.co.in/nget/train-search")
        print(self.driver.title)
        self.driver.close()

    def test_browser_firefox(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.apprenticeship.gov.in/Pages/Apprenticeship/Home.aspx")
        print(self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
