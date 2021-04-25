import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


def calc(num1, num2):
    summ = int(num1) + int(num2)
    return str(summ)


link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element_by_id("num1").text
    num2_element = browser.find_element_by_id("num2").text
    y = calc(num1_element, num2_element)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    quit()

# не забываем оставить пустую строку в конце файла
