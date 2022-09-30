from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    quit()
