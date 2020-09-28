from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_have_add_to_basket_button(self):
        self.is_element_found(*ProductPageLocators.ADD_BUTTON), "'Add To Basket' button not found"

    def add_item_to_basket_click(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket_button.click()
