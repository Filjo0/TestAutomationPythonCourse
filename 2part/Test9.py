import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def calc(num1, num2):
    sum = int(num1) + int(num2)
    return str(sum)


link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1").text
    num2_element = browser.find_element(By.ID, "num2").text
    y = calc(num1_element, num2_element)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    quit()

# не забываем оставить пустую строку в конце файла
