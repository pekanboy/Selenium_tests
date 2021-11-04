from pages.default import DefaultPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage(DefaultPage):
    CLICK_SPEC = '//div[@class="main-buttons__sector"][1]'
    CLICK_CLIENT = '//div[@class="main-buttons__sector"][2]'
    LOGIN_IN_PROFILE = '//div[@class="nickname__text"]'
    REG_SPEC = '//div[@class="specMainContent__title"]'
    REG_CLIENT = '//div[@class="custom-form__label"]'
    PATH = ''

    def click_spec(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_SPEC)

    def click_client(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_CLIENT)

    def wait_registration_spec(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.REG_SPEC)

    def wait_registration_client(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.REG_CLIENT)

    def get_reg_spec(self):
        """
        Получение логина с страницы профиля
        :return: Boolean
        """
        return self.getTextFromElement(self.REG_SPEC)

    def get_reg_client(self):
        """
        Получение логина с страницы профиля
        :return: Boolean
        """
        return self.getTextFromElement(self.REG_CLIENT)

