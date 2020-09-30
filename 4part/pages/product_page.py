import re

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_have_add_to_basket_button(self):
        assert self.is_element_found(*ProductPageLocators.ADD_BUTTON), "'Add To Basket' button not found"

    def add_item_to_basket_click(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket_button.click()

    def should_have_basket_form(self):
        assert self.is_element_found(*ProductPageLocators.BASKET_FORM), "'Basket Form' not found"

    def should_have_price(self):
        assert self.is_element_found(*ProductPageLocators.ITEM_PRICE), "Price for this item not found"

    def price_changed_if_item_added_to_basket(self):
        price = re.findall('([0-9]+[,.]+[0-9]+)', self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text)
        full_amount_basket = re.findall('([0-9]+[,.]+[0-9]+)',
                                        self.browser.find_element(*ProductPageLocators.BASKET_FORM).text)

        alert_item_added = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_ADDED).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        message = item_name

        print(full_amount_basket)
        print(price)
        print(alert_item_added)
        print(item_name)
        assert price == full_amount_basket, "Price for this item is different to price in Basket"
        assert message == alert_item_added, "No message about added item."

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_ADDED), \
            "Success message is presented, but should not have"

    def should_disappear_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.ALERT_SUCCESS_ADDED), "Success message is still presented, but should disappear"
