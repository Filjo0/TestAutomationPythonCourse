import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html "

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = driver.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = driver.find_element(By.ID, "robotCheckbox")
    input2.click()
    people_radio = driver.find_element(By.ID, "peopleRule")
    people_radio.click()

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = driver.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    quit()

# не забываем оставить пустую строку в конце файла
