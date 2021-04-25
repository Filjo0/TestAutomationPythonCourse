import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

main_page = "https://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, main_page)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_have_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, main_page)
        page.open()
        page.should_have_login_link()
