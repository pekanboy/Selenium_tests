from urllib.parse import urljoin

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


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

    def waitOfVisible(self, xpath):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: expected_conditions.visibility_of(d.find_element_by_xpath(xpath))
        )

    def clear_field(self, xpath):
        self.driver.find_element_by_xpath(xpath).clear()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True