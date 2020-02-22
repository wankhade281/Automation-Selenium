from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "userName")
        if elementById is not None:
            print("we found element by Id")
        else:
            print("not a valid Id and throws an Exception unable to locate element")

        elementByXpath = driver.find_element(By.XPATH,"//div[@class='h_menu_drop_button hidden-xs']//i[@class='fa "
                                                      "fa-align-justify']")
        if elementByXpath is not None:
            print("we found element by Xpath")
        else:
            print("not a valid Xpath and throws an Exception unable to locate element")

        elementByLinkText = driver.find_element(By.LINK_TEXT,"CHARTS / VACANCY")
        if elementByLinkText is not None:
            print("we found element by LinkText")
        else:
            print("not a valid LinkText and throws an Exception unable to locate element")


d = ByDemo()
d.test()
