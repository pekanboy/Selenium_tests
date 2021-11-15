from tests.default import DefaultTest
from pages.AuthPage import AuthPage as Page


class AuthTest(DefaultTest):
    def test_auth_user(self):
        """
        Тестирование успешной авторизации пользователя по почте и паролю
        :return:
        """
        self.initPage(Page(self.driver))
        self.auth_client()
        self.page.wait_profile_container()
        login = self.page.get_login_in_profile()
        self.assertEqual(login, self.LOGIN_EXECUTOR, f"Авторизация не прошла")

    def test_err_auth_user(self):
        self.initPage(Page(self.driver))
        self.auth("err_email", "password")
        error_text = self.page.get_error()
        self.assertEqual(
            len(error_text) > 0,
            True,
            f"Сообщение о неудачной авторизации не отобразилось",
        )
