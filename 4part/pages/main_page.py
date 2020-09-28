from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_have_login_link(self):
        assert self.is_element_found(*MainPageLocators.LOGIN_LINK), "Login link not found"
