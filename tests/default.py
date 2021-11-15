import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
import os


class DefaultTest(unittest.TestCase):
    EMAIL_EXECUTOR = os.environ['EMAIL_EXECUTOR']
    PASSWORD_EXECUTOR = os.environ['PASSWORD_EXECUTOR']
    LOGIN_EXECUTOR = os.environ['LOGIN_EXECUTOR']

    EMAIL_CLIENT = os.environ['EMAIL_CLIENT']
    PASSWORD_CLIENT = os.environ['PASSWORD_CLIENT']
    LOGIN_CLIENT = os.environ['LOGIN_CLIENT']

    REG_DATA = {
        "login": os.environ['REG_LOGIN'],
        "name": os.environ['REG_NAME'],
        "email": os.environ['REG_EMAIL'],
        "password": os.environ['REG_PASSWORD'],
    }

    def setUp(self) -> None:
        browser = os.environ.get("BROWSER", "CHROME")

        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
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
