import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    quit()

# не забываем оставить пустую строку в конце файла
