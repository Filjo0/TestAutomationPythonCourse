from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEMS_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_FORM = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ALERT_SUCCESS_ADDED = (By.CLASS_NAME, "alertinner > strong")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
