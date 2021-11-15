from pages.CreateOrderPage import CreateOrderPage
from tests.default import DefaultTest


class CreateOrderTest(DefaultTest):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_SUMM = "//*[contains(text(), 'Недопустимая сумма')]"
    ERR_DATE = "//*[contains(text(), 'Некорректная дата')]"
    ERR_FUTURE = "//*[contains(text(), 'Вряд ли вы столько проживёте...')]"

    def test_create_order(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()

        order_name = "хочу питсы"
        order_budget = 228
        order_deadline = 10102022
        descrioption = "закажите мне питсы"

        self.page.open()
        self.page.fill_header(order_name)
        self.page.fill_budget(order_budget)
        self.page.fill_deadline(order_deadline)
        self.page.select_category()
        self.page.fill_discription(descrioption)
        self.page.submit()
        real_order = self.page.check_create_order()
        self.assertEqual(
            real_order,
            order_name,
            f"Создать заказ не удалось:  имя заказа ${real_order} "
            f"не совпадает с ожидаемым ${order_name}",
        )

    def test_empty_header_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_header("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_long_header_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_header(
            "asfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыа"
        )
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_empty_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_budget("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_long_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_budget(123123123123123)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_deadline_empty_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_deadline("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_DATE)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_deadline_past_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_deadline(10101998)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_DATE)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_deadline_future_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_deadline(10102998)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_FUTURE)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_empty_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_discription("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_long_input(self):
        self.initPage(CreateOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_discription(
            "asdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkska"
        )
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")
