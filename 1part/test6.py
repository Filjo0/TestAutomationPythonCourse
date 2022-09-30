import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Petr")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input5.send_keys("IvanPetrov@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    quit()
