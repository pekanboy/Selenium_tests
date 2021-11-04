from steps.ChangeVacancyStep import ChangeVacancyStep
from tests.default import DefaultTest


class ChangeVacancyrTest(DefaultTest):
    def test_create_vacancy(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        vacancy, expect_vacancy = step.check_change_vacancy()
        self.assertEqual(   vacancy,
                            expect_vacancy,
                            f'Изменить заказ не удалось:  имя заказа ${vacancy} '
                            f'не совпадает с ожидаемым ${expect_vacancy}'
        )

    def test_empty_header_input(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_err = step.check_header_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
        )
    def test_long_header_input(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_err = step.check_header_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
        )
    def test_budget_empty_input(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_err = step.check_budget_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
        )
    def test_budget_long_input(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_err = step.check_budget_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
        )
    def test_descritiopn_empty_input(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_err = step.check_description_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
        )
    def test_descritiopn_long_input(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_err = step.check_description_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
        )
    def test_cancel_button(self):
        self.auth_client()

        step = ChangeVacancyStep(self.driver)
        is_cancel = step.check_cancel_button()
        self.assertEqual(   is_cancel,
                            True,
                            f'Изменения не отменились'
        )