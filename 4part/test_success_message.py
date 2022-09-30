from pages.product_page import ProductPage

link_item = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_item)
    page.open()
    page.should_not_have_success_message()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_item)
    page.open()

    page.add_item_to_basket_click()
    page.should_not_have_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_item)
    page.open()
    page.add_item_to_basket_click()
    page.should_disappear_message()
