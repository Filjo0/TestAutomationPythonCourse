import math
import time

from selenium import webdriver

link = "https://stepik.org/lesson/236895/step/1"

try:
    answer = math.log(int(time.time()))
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(10)

    input1 = browser.find_element_by_css_selector("textarea.textarea")
    input1.send_keys(str(answer))

    button = browser.find_element_by_css_selector("button.submit-submission")

    button.click()
    browser.implicitly_wait(5)

    get_answers = browser.find_element_by_css_selector("pre.smart-hints__hint")
    print(get_answers.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
