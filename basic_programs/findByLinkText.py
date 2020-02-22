from selenium import webdriver


class FindByLinkText:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("CHARTS / VACANCY")
        if elementByLinkText is not None:
            print("we found element by LinkText")
        else:
            print("not a valid LinkText and throws an Exception unable to locate element")

        elementByParText = driver.find_element_by_partial_link_text("CHARTS /")
        if elementByParText is not None:
            print("we found element by Partial Link Text")
        else:
            print("Not an valid Partial Link Text and throws an Exception unable to locate element")


ff = FindByLinkText()
ff.test()
