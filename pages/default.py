from urllib.parse import urljoin


class DefaultPage:
    BASE_URL = 'https://findfreelancer.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def getCookies(self):
        return self.driver.get_cookies()
