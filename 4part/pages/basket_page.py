from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        basket_message = self.browser.find_element(*BasketPageLocators.ITEMS_IN_BASKET_MESSAGE).text
        expected_empty_message = "Your basket is empty. Continue shopping"
        print(basket_message)
        assert basket_message == expected_empty_message, "Basket is not empty"
