import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link = "https://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    quit()
