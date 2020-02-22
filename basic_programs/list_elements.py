from selenium import webdriver


class ListOfElements:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elebyclassname = driver.find_elements_by_class_name("search_btn")
        length = len(elebyclassname)
        if elebyclassname is not None:
            print("Size of list of elements found by class name is: ", length)
        else:
            print("not a valid Id and throws an Exception unable to locate element")

        elebytagname = driver.find_elements_by_tag_name("button")
        length = len(elebytagname)
        if elebytagname is not None:
            print("Size of list of elements found by tag name is: ", length)
        else:
            print("not a valid Id and throws an Exception unable to locate element")


e = ListOfElements()
e.test()
