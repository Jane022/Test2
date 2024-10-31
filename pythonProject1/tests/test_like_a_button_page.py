
from pages.like_a_button_page import LikeAButtonPage


def test_button2_exist(driver):
    like_a_button_page = LikeAButtonPage(driver)
    like_a_button_page.open()
    assert like_a_button_page.like_a_button().is_displayed()

def test_button2_clicked(driver):
    like_a_button_page = LikeAButtonPage(driver)
    like_a_button_page.open()
    like_a_button_page.like_a_button.click()
    assert like_a_button_page.result.text == 'Submitted'
