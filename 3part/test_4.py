import math
import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, links, incorrect_answers=""):
        try:
            answer = math.log(int(time.time()))

            link = f"{links}/"
            browser.get(link)
            browser.implicitly_wait(10)

            input1 = browser.find_element(By.TAG_NAME, "textarea")
            input1.send_keys(str(answer))

            button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")

            button.click()

            get_answers = browser.find_element_by_css_selector("pre.smart-hints__hint").text

            expected = "Correct!"

            browser.implicitly_wait(5)

            assert get_answers == expected, incorrect_answers.join(get_answers)

            print(incorrect_answers)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта

            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
