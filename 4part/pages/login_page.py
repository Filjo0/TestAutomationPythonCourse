from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_have_login_page(self):
        self.should_have_login_url()
        self.should_have_login_form()
        self.should_have_register_form()

    def should_have_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/" \
               in self.browser.current_url, "'Login' not in current url"

    def should_have_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_found(*LoginPageLocators.LOGIN_FORM), "Error. Login form not found"

    def should_have_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_found(*LoginPageLocators.REGISTER_FORM), "Error. Register form not found"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)

        register_button.click()

        successful_registration = self.browser.find_element(*LoginPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE).text
        expected_message = "Thanks for registering!"

        assert successful_registration == expected_message, "Error. User not registered"
