from selenium.webdriver import DesiredCapabilities, Remote
import os
import unittest

from steps.AuthStep import AuthStep


class AuthTest(unittest.TestCase):
    EMAIL = 'test@mail.ru'  # os.environ['EMAIL']
    PASSWORD = '123456Qq'  # os.environ['PASSWORD']
    LOGIN = 'Hello'  # os.environ['LOGIN']

    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_auth_user(self):
        """
        Тестирование успешной авторизации пользователя по почте и паролю
        :return:
        """
        authStep = AuthStep(self.driver)
        authStep.auth(self.EMAIL, self.PASSWORD)
        login = authStep.check_auth()
        self.assertEqual(login,
                         self.LOGIN,
                         f'Авторизоваться не удалось: логин на странице профия ${login} '
                         f'не совпадает с ожидаемым ${self.LOGIN}'
                         )
