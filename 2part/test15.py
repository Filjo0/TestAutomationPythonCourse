import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    browser.get(link)

    button = browser.find_element(By.ID, "book")

    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    quit()
