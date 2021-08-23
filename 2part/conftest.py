import pytest
from selenium import webdriver


def browser():
    print("\nstart browser_chrome for test..")
    browser_chrome = webdriver.Chrome()
    yield browser_chrome
    print("\nquit browser_chrome..")
    browser_chrome.quit()
