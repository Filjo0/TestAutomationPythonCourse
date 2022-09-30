import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    hyperlink = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    hyperlink.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Oleg")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Tomsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    quit()

# не забываем оставить пустую строку в конце файла
