from pages.default import DefaultPage


class AuthPage(DefaultPage):
    PATH = "/login"
    EMAIL_INPUT = '//input[@name="email"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    SUBMIT = '//button[contains(text(),"Войти")]'
    LOGIN_IN_PROFILE = '//div[@class="nickname__text"]'
    ERROR_MESSAGE = '//*[contains(text(),"Неверный логин или пароль")]'

    def fill_Email(self, email):
        """
        Заполнение инпута почты
        :param email:
        :return:
        """
        self.sendKeysOnElement(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        """
        Заполнение инпута пароля
        :param password:
        :return:
        """
        self.sendKeysOnElement(self.PASSWORD_INPUT, password)

    def submit(self):
        """
        Нажатие на кнопку "Войти"
        :return:
        """
        self.clickOnElement(self.SUBMIT)

    def wait_profile_container(self):
        """
        Ожидание отрисовки логина в профиле
        :return:
        """
        self.waitOfVisible(self.LOGIN_IN_PROFILE)

    def get_login_in_profile(self):
        """
        Получение логина с страницы профиля
        :return: Boolean
        """
        return self.getTextFromElement(self.LOGIN_IN_PROFILE)

    def get_error(self):
        self.waitOfVisible(self.ERROR_MESSAGE)
        return self.getTextFromElement(self.ERROR_MESSAGE)
