import time

from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.implicitly_wait(10)
    assert len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form")) > 0, "'Add to basket' button not found"
