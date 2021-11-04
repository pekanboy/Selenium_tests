from pages.default import DefaultPage


class SettingsPage(DefaultPage):
    PATH = '/settings'

    LOGIN_INPUT = '//input[@name="login"]'
    NAME_INPUT = '//input[@name="name"]'
    PASSWORD_INPUT = '//input[@name="oldPassword"]'
    PASSWORD_NEW_INPUT = '//input[@name="password"]'
    PASSWORD_REPEAT_INPUT = '//input[@name="passwordRepeat"]'
    ABOUT = '//textarea[@name="about"]'
    SUBMIT = '//button[@id="send_mess"]'
    ORDER_CREATE_FORM = '//form[@id="order-create_form"]'
    DESCRIPTION =  '//textarea[@name="description"]'

    PROFILE_PAGE_LOGIN = '//span[@class="user-name__text"]'

    def fill_password_repeat(self, password):
        self.sendKeysOnElement(self.PASSWORD_REPEAT_INPUT, password)

    def fill_about(self, about):
        self.sendKeysOnElement(self.ABOUT, about)

    def fill_login(self, login):
        self.sendKeysOnElement(self.LOGIN_INPUT, login)

    def fill_name(self, name):
        self.sendKeysOnElement(self.NAME_INPUT, name)

    def fill_password(self, password):
        self.sendKeysOnElement(self.PASSWORD_INPUT, password)

    def fill_password_new(self, password):
        self.sendKeysOnElement(self.PASSWORD_NEW_INPUT, password)

    def submit(self):
        self.clickOnElement(self.SUBMIT)

    def wait_create_order_form(self):
        self.waitOfVisible(self.ORDER_CREATE_FORM)

    def check_error(self, err):
        return self.check_exists_by_xpath(err)

    def check_change_settings(self):
        self.waitOfVisible(self.PROFILE_PAGE_LOGIN)
        return self.getTextFromElement(self.PROFILE_PAGE_LOGIN)