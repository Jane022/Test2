from pages.button_page import ButtonPage


def test_button1_exist(driver):
    button_page = ButtonPage(driver)
    button_page.open()
    assert button_page.button_is_displayed()

def test_button1_clicked(driver):
    button_page = ButtonPage(driver)
    button_page.open()
    button_page.simple_button().click()
    assert button_page.result_button().text() == 'Submitted'