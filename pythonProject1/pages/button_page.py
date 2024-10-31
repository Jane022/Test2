from pages.base_page import BasePage  #импортируем абстрактный класс
from selenium.webdriver.common.by import By

button_locator = (By.XPATH, '//input[@name="submit"]')  #локатор для кнопки Simple Button
result_locator = (By.ID, 'result-text') #локатор для текста внутри кнопки Simple Button

class ButtonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def simple_button(self):  # кнопка Simple Button
        return self.find(button_locator)

    def button_is_displayed(self):
        return self.simple_button().is_displayed()


    def result_button(self):  # кнопка Result Button
        return self.find(result_locator)

    def open(self):   # метод. открываем страницу
        self.driver.get('https://www.qa-practice.com/elements/button/simple')