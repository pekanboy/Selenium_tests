from steps.default import DefaultStep
from pages.SettingsPage import SettingsPage as Page


class SettingsStep(DefaultStep):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_LOGIN = "//*[contains(text(), 'Неподходящий логин')]"
    ERR_NAME_INCORRECT = "//*[contains(text(), 'Введите имя на кириллице')]"
    ERR_PASSWORD_INCORRECT = "//*[contains(text(), 'Неверный формат')]"
    ERR_PASSWORD_REPEAT_INCORRECT = "//*[contains(text(), 'Пароли не совпадают')]"
    ABOUT_INCORRECT = "//*[contains(text(), 'Сообщение похоже на спам, уберите специальные символы.')]"


    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_change_settings_profile(self):
        login = 'Bars'
        name = 'Олех'
        password = '123456Qq'
        password_new = '123456Qq'
        password_repeat = '123456Qq'
        about = 'абрикос'

        self.page.open()
        self.page.fill_login(login)
        self.page.fill_name(name)
        self.page.fill_password(password)
        self.page.fill_password_new(password_new)
        self.page.fill_password_repeat(password_repeat)
        self.page.fill_about(about)
        self.page.submit()
        return (name, self.page.check_change_settings())

    def check_login_error(self):
        self.page.open()
        self.page.fill_login('абрикос')
        return self.page.check_error(self.ERR_LOGIN)

    def check_name_input_incorrect(self):
        self.page.open()
        self.page.fill_name('bars')
        return self.page.check_error(self.ERR_NAME_INCORRECT)

    def check_password_input(self):
        self.page.open()
        self.page.fill_password('arr')
        return self.page.check_error(self.ERR_PASSWORD_INCORRECT)

    def check_password_new_input(self):
        self.page.open()
        self.page.fill_password_new('arr')
        return self.page.check_error(self.ERR_PASSWORD_INCORRECT)

    def check_password_repeat_input(self):
        self.page.open()
        self.page.fill_password_repeat('arr')
        return self.page.check_error(self.ERR_PASSWORD_REPEAT_INCORRECT)

    def check_about_incorrect_input(self):
        self.page.open()
        self.page.fill_about('<')
        return self.page.check_error(self.ABOUT_INCORRECT)

    def check_about_long_input(self):
        self.page.open()
        self.page.fill_about('asdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkska')
        return self.page.check_error(self.ERR_LENGTH)