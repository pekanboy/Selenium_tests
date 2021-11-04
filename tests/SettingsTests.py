from steps.SettingsStep import SettingsStep
from tests.default import DefaultTest


class SettingsTests(DefaultTest):
    def test_create_order(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        order, expect_order = step.check_change_settings_profile()
        self.assertEqual(   order,
                            expect_order,
                            f'барсук ${order} '
                            f'барс ${expect_order}'
                            )


    def test_about_long_input(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        is_err = step.check_about_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                            )
    def test_about_incorrect_input(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        is_err = step.check_about_incorrect_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                            )

    def test_repeat_password_input(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        is_err = step.check_password_repeat_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                            )

    def test_password_input(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        is_err = step.check_password_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                            )

    def test_name_incorrect_input(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        is_err = step.check_name_input_incorrect()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                            )

    def test_login_input(self):
        self.auth_client()

        step = SettingsStep(self.driver)
        is_err = step.check_login_error()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                            )