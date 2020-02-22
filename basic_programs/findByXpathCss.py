from selenium import webdriver


class FindByXpathCss:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//div[@class='h_menu_drop_button hidden-xs']//i[@class='fa "
                                                      "fa-align-justify']")
        if elementByXpath is not None:
            print("we found element by Xpath")
        else:
            print("not a valid Xpath and throws an Exception unable to locate element")

        elementByCss = driver.find_element_by_css_selector("app-home.ng-star-inserted:nth-child(2) "
                                                           "app-header:nth-child(1) div.h_container_sm:nth-child(4) "
                                                           "div.h_menu_drop_button.hidden-xs:nth-child(3) "
                                                           "a:nth-child(1) > i.fa.fa-align-justify")
        if elementByCss is not None:
            print("we found element by Css selector")
        else:
            print("Not an valid Css selector and throws an Exception unable to locate element")


ff = FindByXpathCss()
ff.test()
