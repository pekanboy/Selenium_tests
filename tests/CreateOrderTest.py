from steps.CreateOrderStep import CreateOrderStep
from tests.default import DefaultTest


class CreateOrderTest(DefaultTest):
    def test_create_order(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        order, expect_order = step.check_create_order()
        self.assertEqual(   order,
                            expect_order,
                            f'Создать заказ не удалось:  имя заказа ${order} '
                            f'не совпадает с ожидаемым ${expect_order}'
                        )

    def test_empty_header_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_header_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_long_header_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_header_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_budget_empty_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_budget_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_budget_long_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_budget_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_deadline_empty_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_deadline_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )

    def test_deadline_past_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_deadline_past_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_deadline_future_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_deadline_future_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_descritiopn_empty_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_description_empty_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )
    def test_descritiopn_long_input(self):
        self.auth_client()

        step = CreateOrderStep(self.driver)
        is_err = step.check_description_long_input()
        self.assertEqual(   is_err,
                            True,
                            f'Ошибка инпута не появилась'
                        )