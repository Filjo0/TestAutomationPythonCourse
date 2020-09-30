import pytest
from pages.product_page import ProductPage


# link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize('promo_code',
                         [
                             0, 1, 2,
                             3, 4, 5, 6,
                             7, 8, 9
                         ])
def test_guest_can_add_product_to_basket(browser, promo_code):
    product_url = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, product_url)
    page.open()
    page.should_have_add_to_basket_button()
    page.should_have_basket_form()
    page.should_have_price()

    page.add_item_to_basket_click()
    page.solve_quiz_and_get_code()
    page.price_changed_if_item_added_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_have_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
