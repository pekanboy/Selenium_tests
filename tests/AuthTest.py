from tests.default import DefaultTest


class AuthTest(DefaultTest):
    def test_auth_user(self):
        """
        Тестирование успешной авторизации пользователя по почте и паролю
        :return:
        """
        authStep = self.auth()
        login = authStep.check_auth()
        self.assertEqual(login,
                         self.LOGIN,
                         f'Авторизоваться не удалось: логин на странице профия ${login} '
                         f'не совпадает с ожидаемым ${self.LOGIN}'
                         )
