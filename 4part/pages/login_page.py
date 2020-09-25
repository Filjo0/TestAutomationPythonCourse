from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_have_login_page(self):
        self.should_have_login_url()
        self.should_have_login_form()
        self.should_have_register_form()

    def should_have_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" \
               in self.browser.current_url, "'login' not in current url"

    def should_have_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_found(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_have_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_found(*LoginPageLocators.REGISTER_FORM), "Register form not found"
