from steps.default import DefaultStep
from pages.NavbarsPage import NavbarsPage as Page


class NavbarsStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_redirect_vacancy(self):
        """
        Проверка на редирект страницу создания вакансии за исполнителя
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_vacancy_button()
        self.page.wait_vacancy()
        return True

    def check_redirect_order(self):
        """
        Проверка на редирект страницу создания заказа за клиента
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_order_button()
        self.page.wait_order()
        return True

    def check_redirect_logo(self):
        """
        Проверка на редирект страницу профиля при нажатии на логотип
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_logo()
        self.page.wait_logo()
        return True

    def check_redirect_person(self):
        """
        Проверка на редирект страницу создания заказа за клиента
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_person()
        self.page.wait_person()
        return True

    def check_redirect_loop(self):
        """
        Проверка на редирект страницу профиля при нажатии на логотип
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_loop()
        self.page.wait_loop()
        return True

    def check_redirect_vacancies_spec(self):
        """
        Проверка на редирект страницу создания заказа за клиента
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_vacancies_spec()
        self.page.wait_vacancies_spec()
        return True

    def check_redirect_orders_spec(self):
        """
        Проверка на редирект страницу профиля при нажатии на логотип
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_orders_spec()
        self.page.wait_orders_spec()
        return True

    def check_redirect_reg_client(self):
        """
        Проверка на редирект страницу создания заказа за клиента
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_reg()
        self.page.click_reg_client()
        self.page.wait_reg_client()
        return True

    def check_redirect_reg_spec(self):
        """
        Проверка на редирект страницу профиля при нажатии на логотип
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_reg()
        self.page.click_reg_spec()
        self.page.wait_reg_spec()
        return True

    def check_redirect_login(self):
        """
        Проверка на редирект страницу профиля при нажатии на логотип
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_login()
        self.page.wait_login()
        return True