import time
import unittest

from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input5.send_keys("Petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" is welcome_text,
                         False)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Input your name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input5.send_keys("Petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" is welcome_text,
                         False)


if __name__ == "__main__":
    unittest.main()
