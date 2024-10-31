from pages.base_page import BasePage
from selenium.webdriver.common.by import By

like_a_button_locator = (By.LINK_TEXT, 'Click')
result_locator = (By.ID, 'result-text')

class LikeAButtonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/button/like_a_button')

    @property
    def like_a_button(self):
        return self.find(like_a_button_locator)

    def click(self):
        self.like_a_button.click()

    @property
    def result(self):
        return self.find(result_locator)


