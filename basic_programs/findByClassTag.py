from selenium import webdriver


class FindByClassTag:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByclassname = driver.find_element_by_class_name("")
        if elementByclassname is not None:
            print("we found element by Class Name")
        else:
            print("not a valid Class Name and throws an Exception unable to locate element")

        elementBytagname = driver.find_element_by_tag_name("")
        if elementBytagname is not None:
            print("we found element by Tag Name")
        else:
            print("Not an valid Tag Name and throws an Exception unable to locate element")


ff = FindByClassTag()
ff.test()
