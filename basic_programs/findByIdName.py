from selenium import webdriver


class FindByIdName:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/profile/user-registration"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("userName")
        if elementById is not None:
            print("we found element by Id")
        else:
            print("not a valid Id and throws an Exception unable to locate element")

        elementByName = driver.find_element_by_name("userName")
        if elementByName is not None:
            print("we found element by Name")
        else:
            print("not a valid Name and throws an Exception unable to locate element")


ff = FindByIdName()
ff.test()
