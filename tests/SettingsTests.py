from pages.SettingsPage import SettingsPage as Page
from tests.default import DefaultTest


class SettingsTests(DefaultTest):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_LOGIN = "//*[contains(text(), 'Неподходящий логин')]"
    ERR_NAME_INCORRECT = "//*[contains(text(), 'Введите имя на кириллице')]"
    ERR_PASSWORD_INCORRECT = "//*[contains(text(), 'Неверный формат')]"
    ERR_PASSWORD_REPEAT_INCORRECT = "//*[contains(text(), 'Пароли не совпадают')]"
    ABOUT_INCORRECT = "//*[contains(text(), 'Сообщение похоже на спам, уберите специальные символы.')]"

    def test_create_order(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        login = 'Bars'
        name = 'Олех'
        password = 'Vbrhjajy1878'
        password_new = 'Vbrhjajy1878'
        password_repeat = 'Vbrhjajy1878'
        about = 'абрикос'

        self.page.open()
        self.page.fill_login(login)
        self.page.fill_name(name)
        self.page.fill_password(password)
        self.page.fill_password_new(password_new)
        self.page.fill_password_repeat(password_repeat)
        self.page.fill_about(about)
        self.page.submit()

        order, expect_order = (name, self.page.check_change_settings())
        self.assertEqual(order,
                         expect_order,
                         f'барсук ${order} '
                         f'барс ${expect_order}'
                         )

    def test_about_long_input(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        self.page.open()
        self.page.fill_about(
            'asdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkska')

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err,
                         True,
                         f'Ошибка инпута не появилась'
                         )

    def test_about_incorrect_input(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        self.page.open()
        self.page.fill_about('<')
        is_err = self.page.check_error(self.ABOUT_INCORRECT)
        self.assertEqual(is_err,
                         True,
                         f'Ошибка инпута не появилась'
                         )

    def test_repeat_password_input(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        self.page.open()
        self.page.fill_password_repeat('arr')
        is_err = self.page.check_error(self.ERR_PASSWORD_REPEAT_INCORRECT)
        self.assertEqual(is_err,
                         True,
                         f'Ошибка инпута не появилась'
                         )

    def test_password_input(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        self.page.open()
        self.page.fill_password('arr')
        is_err = self.page.check_error(self.ERR_PASSWORD_INCORRECT)
        self.assertEqual(is_err,
                         True,
                         f'Ошибка инпута не появилась'
                         )

    def test_name_incorrect_input(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        self.page.open()
        self.page.fill_name('bars')
        is_err = self.page.check_error(self.ERR_NAME_INCORRECT)
        self.assertEqual(is_err,
                         True,
                         f'Ошибка инпута не появилась'
                         )

    def test_login_input(self):
        self.initPage(Page(self.driver))
        self.auth_client()

        self.page.open()
        self.page.fill_login('абрикос')
        is_err = self.page.check_error(self.ERR_LOGIN)
        self.assertEqual(is_err,
                         True,
                         f'Ошибка инпута не появилась'
                         )
