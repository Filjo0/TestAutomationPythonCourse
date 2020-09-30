from pages.basket_page import BasketPage

main_page = "http://selenium1py.pythonanywhere.com/"
link_the_city_stars = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    page = BasketPage(browser, main_page)
    page.open()
    page.should_have_basket_button()
    page.go_to_basket_page()
    page.is_basket_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link_the_city_stars)
    page.open()
    page.should_have_basket_button()
    page.go_to_basket_page()
    page.is_basket_empty()
