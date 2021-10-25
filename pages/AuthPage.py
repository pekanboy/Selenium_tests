from pages.default import DefaultPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Auth(DefaultPage):
    PATH = '/login'
    EMAIL_INPUT = '//input[@name="email"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    SUBMIT = '//button[contains(text(),"Войти")]'
    LOGIN_IN_PROFILE = '//div[@class="nickname__text"]'

    def fill_Email(self, email):
        """
        Заполнение инпута почты
        :param email:
        :return:
        """
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        """
        Заполнение инпута пароля
        :param password:
        :return:
        """
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        """
        Нажатие на кнопку "Войти"
        :return:
        """
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def wait_profile_container(self):
        """
        Ожидание отрисовки логина в профиле
        :return:
        """
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: expected_conditions.visibility_of(d.find_element_by_xpath(self.LOGIN_IN_PROFILE))
        )

    def get_login_in_profile(self):
        """
        Получение логина с страницы профиля
        :return: Boolean
        """
        return self.driver.find_element_by_xpath(self.LOGIN_IN_PROFILE).text

