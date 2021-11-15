import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
import os


class DefaultTest(unittest.TestCase):
    EMAIL_EXECUTOR = 'test_ex@mail.ru'
    PASSWORD_EXECUTOR = '123456Qq'  # os.environ['PASSWORD']
    LOGIN_EXECUTOR = 'Bars'

    EMAIL_CLIENT = 'kek228@mail.ru'  # os.environ['EMAIL_CLIENT']
    PASSWORD_CLIENT = 'Vbrhjajy1878'  # os.environ['PASSWORD_CLIENT']
    LOGIN_CLIENT = 'kek228'  # os.environ['LOGIN_CLIENT']
    
    REG_DATA = {
        'login': 'qwerty',
        'name': 'Тест',
        'email': 'asdas12d@test.ru',
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

    def auth_executor(self):
        auth = AuthPage(self.driver)
        self.auth(self.EMAIL_EXECUTOR, self.PASSWORD_EXECUTOR)
        auth.wait_profile_container()

    def auth_client(self):
        auth = AuthPage(self.driver)
        self.auth(self.EMAIL_CLIENT, self.PASSWORD_CLIENT)
        auth.wait_profile_container()

    def auth(self, email, password):
        auth = AuthPage(self.driver)
        auth.open()
        auth.fill_Email(email)
        auth.fill_password(password)
        auth.submit()

    def initPage(self, page):
        self.page = page
