from steps.default import DefaultStep
from pages.MainPage import MainPage as Page


class MainStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_redirect_spec(self):
        """
        Проверка на редирект страницу регистрации за исполнителя
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_spec()
        self.page.wait_registration_spec()
        return self.page.get_reg_spec()

    def check_redirect_client(self):
        """
        Проверка на редирект страницу регистрации за клиента
        :return: string: логин со страницы пользователя
        """
        self.page.open()
        self.page.click_client()
        self.page.wait_registration_client()
        return self.page.get_reg_client()
