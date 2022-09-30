from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def browser():
    print("\nstart browser_chrome for test..")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    print("\nquit browser..")
    driver.quit()
