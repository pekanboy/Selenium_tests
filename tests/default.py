import unittest
from selenium.webdriver import DesiredCapabilities, Remote
import os

from steps.AuthStep import AuthStep


class DefaultTest(unittest.TestCase):
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

    def auth(self):
        authStep = AuthStep(self.driver)
        authStep.auth(self.EMAIL, self.PASSWORD)
        return authStep
