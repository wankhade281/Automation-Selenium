from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/ul/li[5]/a/label").click()
driver.maximize_window()
driver.close()
# driver.quit()

























# import testcases
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
#
# class PythonOrgSearch(testcases.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#     def tearDown(self):
#         self.driver.close()
#
#
# if __name__ == "__main__":
#     testcases.main()
