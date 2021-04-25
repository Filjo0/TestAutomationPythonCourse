import time

import pytest
from mimesis import Person

from pages.login_page import LoginPage
from pages.product_page import ProductPage

link_no_offers = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
link_the_city_stars = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
products_url = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_no_offers)
        page.open()

        page.add_item_to_basket_click()
        page.should_not_have_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_the_city_stars)
        page.open()
        page.should_have_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_the_city_stars)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_code',
                             [
                                 0, 1, 2,
                                 3, 4, 5, 6,
                                 7, 8, 9
                             ])
    def test_guest_can_add_product_to_basket(self, browser, promo_code):
        products_url.format(promo_code)
        page = ProductPage(browser, products_url)
        page.open()
        page.should_have_add_to_basket_button()
        page.should_have_basket_form()
        page.should_have_price()

        page.add_item_to_basket_click()
        page.solve_quiz_and_get_code()
        page.price_changed_if_item_added_to_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        person = Person('en')
        self.email = person.email()
        self.password = person.password(9)

    def test_user_can_register(self, browser):
        page = ProductPage(browser, link_no_offers)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(self.email, self.password)
        time.sleep(30)

    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_code',
                             [
                                 0, 1, 2,
                                 3, 4, 5, 6,
                                 7, 8, 9
                             ])
    def test_user_can_add_product_to_basket(self, browser, promo_code):
        products_url.format(promo_code)
        page = ProductPage(browser, products_url)
        page.open()
        page.should_have_add_to_basket_button()
        page.should_have_basket_form()
        page.should_have_price()

        page.add_item_to_basket_click()
        page.solve_quiz_and_get_code()
        page.price_changed_if_item_added_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_no_offers)
        page.open()
        page.should_not_have_success_message()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_no_offers)
        page.open()

        page.add_item_to_basket_click()
        page.should_not_have_success_message()
