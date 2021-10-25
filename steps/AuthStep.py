from steps.default import DefaultStep
from pages.AuthPage import AuthPage as Page


class AuthStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_auth(self):
        """
        Проверка на аворизацию пользователя
        :return: string: логин со страницы пользователя
        """
        self.page.wait_profile_container()
        return self.page.get_login_in_profile()
