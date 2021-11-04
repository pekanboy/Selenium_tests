from steps.AuthStep import AuthStep
from tests.default import DefaultTest


class AuthTest(DefaultTest):
    def test_auth_user(self):
        """
        Тестирование успешной авторизации пользователя по почте и паролю
        :return:
        """
        authStep = self.auth_client()
        login = authStep.check_auth()
        self.assertEqual(login,
                         self.LOGIN,
                         f'Авторизоваться не удалось: логин на странице профия ${login} '
                         f'не совпадает с ожидаемым ${self.LOGIN}'
                         )

    def test_err_auth_user(self):
        authStep = AuthStep(self.driver)
        authStep.check_err_auth()
