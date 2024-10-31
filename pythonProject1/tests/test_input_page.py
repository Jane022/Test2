# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
#
# def test_input_field(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_string = driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')
#     text_string.send_keys('Privetik')
#     text_string.send_keys(Keys.ENTER)
#     sleep(5)
#
# def test_clear_input_field(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_string = driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')
#     text_string.send_keys('Privetik')
#     input_text = text_string.get_attribute('value')
#     for _ in range (len(input_text)):
#         text_string.send_keys(Keys.BACKSPACE)
#     sleep(5)