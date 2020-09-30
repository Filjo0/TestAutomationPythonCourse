from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_FORM = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ALERT_SUCCESS_ADDED = (By.CLASS_NAME, "alertinner > strong")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
