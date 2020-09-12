import time

import requests
from bs4 import BeautifulSoup

try:
    r = requests.get("https://www.whoscored.com/Previews")
    soup = BeautifulSoup(r.content, "html.parser")

    for a_tag in soup.find_all('a', href=True, attrs={'class': 'main'}):
        print('href: ', a_tag['href'])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    quit()
