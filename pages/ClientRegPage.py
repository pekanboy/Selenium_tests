from pages.default import DefaultPage


class ClientRegPage(DefaultPage):
    PATH = '/client-reg'

    LOGIN_INPUT = '//input[@name="login"]'
    LOGIN_ERROR = '//*[contains(text(),"Неподходящий логин")]'
    NAME_INPUT = '//input[@name="name"]'
    NAME_ERROR_LENGTH = '//*[contains(text(),"Недопустимая длина")]'
    NAME_ERROR_LANG = '//*[contains(text(),"Введите имя на кириллице")]'
    EMAIL_INPUT = '//input[@name="email"]'
    EMAIL_ERROR = '//*[contains(text(),"Неверный формат электронной почты")]'
    PASSWORD_INPUT = '//input[@name="password"]'
    PASSWORD_ERROR = '//*[contains(text(),"Неверный формат")]'
    PASSWORD_REPEAT_INPUT = '//input[@name="passwordRepeat"]'
    PASSWORD_REPEAT_ERROR = '//*[contains(text(),"Пароли не совпадают")]'

    SUBMIT = '//*[@id="send_mess"]'

    LOGIN_IN_PROFILE = '//div[@class="nickname__text"]'

    def fill_login(self, login):
        return self.fill(self.LOGIN_INPUT, login)

    def fill_name(self, name):
        return self.fill(self.NAME_INPUT, name)

    def fill_email(self, email):
        return self.fill(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        return self.fill(self.PASSWORD_INPUT, password)

    def fill_repeat_password(self, password):
        return self.fill(self.PASSWORD_REPEAT_INPUT, password)

    def check_error_login(self):
        return self.getTextFromElement(self.LOGIN_ERROR)

    def check_error_name_lang(self):
        return self.getTextFromElement(self.NAME_ERROR_LANG)

    def check_error_name_length(self):
        return self.getTextFromElement(self.NAME_ERROR_LENGTH)

    def check_error_email(self):
        return self.getTextFromElement(self.EMAIL_ERROR)

    def check_error_password(self):
        return self.getTextFromElement(self.PASSWORD_ERROR)

    def check_error_password_repeat(self):
        return self.getTextFromElement(self.PASSWORD_REPEAT_ERROR)

    def submit(self):
        self.clickOnElement(self.SUBMIT)

    def get_login_in_profile(self):
        return self.getTextFromElement(self.LOGIN_IN_PROFILE)
