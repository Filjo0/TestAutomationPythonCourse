from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = BasketPage(browser, link)
    page.open()
    page.should_have_cart_button()
    page.go_to_cart_page()
    page.is_basket_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_have_cart_button()
    page.go_to_cart_page()
    page.is_basket_empty()
