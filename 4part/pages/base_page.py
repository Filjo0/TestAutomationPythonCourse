import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_found(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_have_login_link(self):
        assert self.is_element_found(*BasePageLocators.LOGIN_LINK), "Login link does not exist"

    def go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        button.click()

    def should_have_basket_button(self):
        assert self.is_element_found(*BasePageLocators.BASKET_BUTTON), "Basket button does not exist"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_found(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                   " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
