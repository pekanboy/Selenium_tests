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

    def get_cookies(self):
        return self.driver.get_cookies()

    def clickOnElement(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def sendKeysOnElement(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def getTextFromElement(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text
