import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAbs:
    def test_abs1(self, browser):
        link = "https://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input5.send_keys("Petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == "Congratulations! You have successfully registered!"

    def test_abs2(self, browser):
        link = "https://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input5.send_keys("Petrov@mail.ru")

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
        assert welcome_text == "Congratulations! You have successfully registered!"
