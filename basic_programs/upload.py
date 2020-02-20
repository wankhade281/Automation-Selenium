from selenium import webdriver
import time


class Upload:
    def upload(self):
        driver = webdriver.Chrome()  # opens the chrome driver
        driver.maximize_window()

        driver.get('https://www.linkedin.com/')  # opens the browser with
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("nav__button-secondary").click()
        time.sleep(5)
        driver.find_element_by_id("username").send_keys("wankhadechetan281@gmail.com")
        driver.find_element_by_id("password").send_keys("Chetan@95")
        driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='ember26']").click()
        driver.find_element_by_xpath("//span[@class='artdeco-button artdeco-button--tertiary artdeco-button--fluid']").click()
        driver.find_element_by_xpath("//button[@class='pv-top-card__edit-photo-button']").click()
        driver.find_element_by_id("image-selector__file-upload-input").send_keys("/home/admin1/Downloads/download.jpeg")
        driver.find_element_by_xpath("//span[text()='Save photo']").click()
        time.sleep(5)


if __name__ == '__main__':
    u = Upload()
    u.upload()

# from selenium import webdriver
# import time
#
#
# class Upload:
#     def upload(self):
#         driver = webdriver.Chrome()  # opens the chrome driver
#         driver.maximize_window()
#
#         driver.get('http://testautomationpractice.blogspot.com/')  # opens the browser with
#         driver.switch_to_frame(0)
#         scroll = driver.find_element_by_id("RESULT_FileUpload-10")
#         driver.execute_script("arguments[0].scrollIntoView();",scroll)
#         time.sleep(5)
#         driver.find_element_by_id("RESULT_FileUpload-10").send_keys("/home/admin1/Downloads/download.jpeg")
#         time.sleep(5)
#
#
# if __name__ == '__main__':
#     u = Upload()
#     u.upload()
