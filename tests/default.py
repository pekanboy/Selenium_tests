import unittest
from selenium.webdriver import DesiredCapabilities, Remote
import os

from steps.AuthStep import AuthStep


class DefaultTest(unittest.TestCase):
    EMAIL = 'test@mail.com'  # os.environ['EMAIL']
    PASSWORD = '123456Qq'  # os.environ['PASSWORD']
    LOGIN = 'Hello'  # os.environ['LOGIN']

    EMAIL_EXECUTOR = 'test_ex@mail.ru'
    PASSWORD_EXECUTOR = '123456Qq'  # os.environ['PASSWORD']
    LOGIN_EXECUTOR = 'test'

    REG_DATA = {
        'login': 'qwerty',
        'name': 'Тест',
        'email': 'emastgdtl@test.ru',
        'password': '123456Qq'
    }

    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def auth_client(self):
        authStep = AuthStep(self.driver)
        authStep.auth(self.EMAIL, self.PASSWORD)
        authStep.page.wait_profile_container()
        return authStep

    def auth_executor(self):
        authStep = AuthStep(self.driver)
        authStep.auth(self.EMAIL_EXECUTOR, self.PASSWORD_EXECUTOR)
        authStep.page.wait_profile_container()
        return authStep
