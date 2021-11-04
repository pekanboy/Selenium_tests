from selenium.webdriver import Keys

from steps.default import DefaultStep
from pages.ClientRegPage import ClientRegPage as Page


class ClientRegStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_err_login(self):
        self.page.open()
        err_login = '<>'

        self.page.fill_login(err_login)
        self.page.check_error_login()

    def check_err_name(self):
        self.page.open()
        err_name = 'q'

        self.page.fill_name(err_name)
        self.page.check_error_name_lang()

        self.page.fill_name(Keys.BACKSPACE)
        self.page.check_error_name_length()

    def check_err_email(self):
        self.page.open()
        err_email = ['<>', 'testtest@mail.']

        for email in err_email:
            self.page.fill_email(email)
            self.page.check_error_email()

    def check_err_password(self):
        self.page.open()
        err_pswd = '123456'
        ok_pswd = '123456Ww'

        self.page.fill_password(err_pswd)
        self.page.check_error_password()

        self.page.fill_password(ok_pswd)
        self.page.fill_repeat_password(err_pswd)
        self.page.check_error_password_repeat()

    def good_register(self, data):
        self.page.open()

        self.page.fill_login(data['login'])
        self.page.fill_name(data['name'])
        self.page.fill_email(data['email'])
        self.page.fill_password(data['password'])
        self.page.fill_repeat_password(data['password'])
        self.page.submit()

        setting_login = self.page.get_login_in_profile()

        return setting_login == data['login']
