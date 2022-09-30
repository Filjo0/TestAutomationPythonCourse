import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()

    button.click()
    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    quit()
