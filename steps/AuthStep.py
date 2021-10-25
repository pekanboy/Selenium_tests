from steps.default import DefaultStep
from pages.AuthPage import Auth as Page


class AuthStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def auth(self, email, password):
        """
        Воспроизведение по шагам авторизации пользователя
        :param email:
        :param password:
        :return:
        """
        self.page.open()
        self.page.fill_Email(email)
        self.page.fill_password(password)
        self.page.submit()

    def check_auth(self):
        """
        Проверка на аворизацию пользователя
        :return: string: логин со страницы пользователя
        """
        self.page.wait_profile_container()
        return self.page.get_login_in_profile()
