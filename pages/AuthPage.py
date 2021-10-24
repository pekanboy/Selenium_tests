from pages.default import DefaultPage
from selenium.webdriver.support.ui import WebDriverWait


class Auth(DefaultPage):
    PATH = '/login'
    EMAIL_INPUT = '//input[@name="email"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    SUBMIT = '//button[contains(text(),"Войти")]'
    PROFILE_CONTAINER = '//div[@class="profile"]'

    def fillEmail(self, email):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)

    def fillPassword(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def waitProfileContainer(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PROFILE_CONTAINER)
        )

