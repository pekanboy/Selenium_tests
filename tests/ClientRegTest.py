from tests.default import DefaultTest
from pages.ClientRegPage import ClientRegPage as Page


class ClientRegTest(DefaultTest):
    def test_login(self):
        self.initPage(Page(self.driver))

        self.page.open()
        err_login = "<>"

        self.page.fill_login(err_login)
        error_text = self.page.check_error_login()
        self.assertEqual(
            len(error_text) > 0,
            True,
            "Сообщение об ошибке неверного логина не отобразилось",
        )

    def test_name(self):
        self.initPage(Page(self.driver))

        self.page.open()
        err_name = "q"

        self.page.fill_name(err_name)
        error_text = self.page.check_error_name_lang()
        self.assertEqual(
            len(error_text) > 0,
            True,
            "Сообщение об ошибке неверного имени не отобразилось",
        )

    def test_email(self):
        self.initPage(Page(self.driver))

        self.page.open()
        err_email = ["<>", "testtest@mail."]

        for email in err_email:
            self.page.fill_email(email)
            error_text = self.page.check_error_email()
            self.assertEqual(
                len(error_text) > 0,
                True,
                "Сообщение об ошибке неверной почты не отобразилось",
            )

    def test_password(self):
        self.initPage(Page(self.driver))

        self.page.open()
        err_pswd = "123456"
        ok_pswd = "123456Ww"

        self.page.fill_password(err_pswd)
        error_text = self.page.check_error_password()
        self.assertEqual(
            len(error_text) > 0,
            True,
            "Сообщение об ошибке неверного пароля не отобразилось",
        )

        self.page.fill_password(ok_pswd)
        self.page.fill_repeat_password(err_pswd)
        error_text = self.page.check_error_password_repeat()
        self.assertEqual(
            len(error_text) > 0,
            True,
            "Сообщение об ошибке неверного повторного пароля не отобразилось",
        )

    def test_good_registration(self):
        self.initPage(Page(self.driver))

        self.page.open()

        self.page.fill_login(self.REG_DATA["login"])
        self.page.fill_name(self.REG_DATA["name"])
        self.page.fill_email(self.REG_DATA["email"])
        self.page.fill_password(self.REG_DATA["password"])
        self.page.fill_repeat_password(self.REG_DATA["password"])
        self.page.submit()

        setting_login = self.page.get_login_in_profile()
        self.assertEqual(
            setting_login, self.REG_DATA["login"], "Не удалось зарегестрироваться"
        )
