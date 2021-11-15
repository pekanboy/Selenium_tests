from pages.default import DefaultPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class NavbarsPage(DefaultPage):
    CLICK_VACANCY = '//div[@class="row"]/button[1]'
    CLICK_ORDER = '//div[@class="row"]/button[2]'
    CLICK_LOGO = '//a[@class="navbar__title"]'
    CLICK_PERSON = '//div[@class="row__item"][1]'
    CLICK_LOOP = '//div[@class="row__item"][2]'
    CLICK_VACANCIES_SPEC = '//div[@class="row"]/button[2]'
    CLICK_ORDERS_SPEC = '//div[@class="row"]/button[1]'
    CLICK_REG_CLIENT = '//div[@class="navbar__registration_content"]/a[1]'
    CLICK_REG_SPEC = '//div[@class="navbar__registration_content"]/a[2]'
    CLICK_REG = '//div[@class="navbar__registration_text"]/a[1]'
    CLICK_LOGIN = '//a[@class="navbar__enter_text"]'
    VACANCY = '//div[@class="create__bg-form"][1]'
    ORDER = '//div[@class="create__bg-form"][1]'
    LOGO = '//div[@class="profile"]'
    LOOP = '//div[@class="orders"]'
    VACANCIES_SPEC = '//div[@class="orders__content"]'
    ORDERS_SPEC = '//div[@class="orders__list"]'
    REG_CLIENT = '//div[@class="custom-form__label"]'
    REG_SPEC = '//div[@class="specMainContent__select"]'
    LOGIN = '//div[@class="custom-form__label"]'
    PATH = ''

    def click_login(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_LOGIN)

    def click_reg(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_REG)

    def click_reg_client(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_REG_CLIENT)

    def click_reg_spec(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_REG_SPEC)

    def click_vacancy_button(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_VACANCY)

    def click_order_button(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_ORDER)

    def click_logo(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_LOGO)

    def click_loop(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_LOOP)

    def click_person(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_PERSON)

    def click_vacancies_spec(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_VACANCIES_SPEC)

    def click_orders_spec(self):
        """
        Клик по ссылке
        :return:
        """
        self.clickOnElement(self.CLICK_ORDERS_SPEC)

    def wait_vacancy(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.VACANCY)

    def wait_order(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.ORDER)

    def wait_logo(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.LOGO)

    def wait_person(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.LOGO)

    def wait_loop(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.LOOP)

    def wait_vacancies_spec(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.VACANCIES_SPEC)

    def wait_orders_spec(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.ORDERS_SPEC)

    def wait_reg_client(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.REG_CLIENT)

    def wait_reg_spec(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.REG_SPEC)

    def wait_login(self):
        """
        Ожидание отрисовки регистрации
        :return:
        """
        self.waitOfVisible(self.LOGIN)