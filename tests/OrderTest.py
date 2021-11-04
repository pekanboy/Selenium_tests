from steps.OrderStep import OrderStep 
from tests.default import DefaultTest


class OrderTest(DefaultTest):
    def test_select_executor(self):
        self.auth_client()

        step = OrderStep(self.driver)
        is_select = step.check_select_executor()
        self.assertEqual(   is_select,
                            True,
                            f'Исполнитель не выбрался'
                        )

    def test_cancel_executor(self):
        self.auth_client()

        step = OrderStep(self.driver)
        is_cancel = step.check_cancel_executor()
        self.assertEqual(   is_cancel,
                            True,
                            f'Не получилось отказатсья от исполнителя'
                        )
    def test_change_order_window(self):
        self.auth_client()

        step = OrderStep(self.driver)
        is_open = step.check_change_order()
        self.assertEqual(   is_open,
                            True,
                            f'Окно изменения заказа не открылось'
                        )
    def test_end_order(self):
        self.auth_client()

        step = OrderStep(self.driver)
        is_open = step.check_end_order()
        self.assertEqual(   is_open,
                            True,
                            f'Окно подтверждения завершения заказа не появилось'
                        )

    def test_no_end_button(self):
        self.auth_client()

        step = OrderStep(self.driver)
        is_close = step.check_no_end_button()
        self.assertEqual(is_close,
                            True,
                            f'Окно подтверджения завершения заказа не закрылось'
                        )
