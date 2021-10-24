from steps.default import DefaultStep
from pages.AuthPage import Auth as Page


class AuthStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def auth(self, email, password):
        self.page.open()
        self.page.fillEmail(email)
        self.page.fillPassword(password)
        self.page.submit()

    def checkAuth(self):
        self.page.waitProfileContainer()
