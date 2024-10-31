from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find(self, args):
        return self.driver.find_element(*args)