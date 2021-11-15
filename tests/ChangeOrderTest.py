from pages.ChangeOrderPage import ChangeOrderPage
from tests.default import DefaultTest
import random
import string


class ChangeOrderTest(DefaultTest):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_SUMM = "//*[contains(text(), 'Недопустимая сумма')]"
    ERR_DATE = "//*[contains(text(), 'Некорректная дата')]"
    ERR_FUTURE = "//*[contains(text(), 'Вряд ли вы столько проживёте...')]"
    CHANGE_BUTTON = '//button[@class="vacancyPage__customer-button_change"]'
    SETTINGS_LABEL = '//div[@class="settings__label"]'

    def test_change_order(self):
        self.initPage(ChangeOrderPage(self.driver))

        self.auth_client()
        letters = string.ascii_lowercase
        result_str = "".join(random.choice(letters) for i in range(10))
        order_name = "хочу многа питсы" + result_str
        order_budget = 228
        order_deadline = 10102022
        descrioption = "закажите мне питсы но теперь побольше"

        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)

        self.page.clear_header()
        self.page.clear_budget()
        self.page.clear_deadline()
        self.page.clear_description()

        self.page.fill_header(order_name)
        self.page.fill_budget(order_budget)
        self.page.fill_deadline(order_deadline)
        self.page.select_category()
        self.page.fill_discription(descrioption)
        self.page.submit()
        result_order = self.page.check_change_order()
        self.assertEqual(
            result_order,
            order_name,
            f"Изменить заказ не удалось:  имя заказа ${order_name} "
            f"не совпадает с ожидаемым ${result_order}",
        )

    def test_empty_header_input(self):
        self.initPage(ChangeOrderPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_header()
        self.page.fill_header("")
        self.page.select_category()
        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_long_header_input(self):
        self.initPage(ChangeOrderPage(self.driver))
        self.auth_client()

        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_header()
        self.page.fill_header(
            "asfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыа"
        )
        self.page.select_category()
        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_empty_input(self):
        self.initPage(ChangeOrderPage(self.driver))

        self.auth_client()
        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_budget()
        self.page.fill_budget("")
        self.page.select_category()
        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_long_input(self):
        self.initPage(ChangeOrderPage(self.driver))

        self.auth_client()
        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_budget()
        self.page.fill_budget(123123123123123)
        self.page.select_category()
        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_deadline_empty_input(self):
        self.initPage(ChangeOrderPage(self.driver))

        self.auth_client()
        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_deadline()
        self.page.fill_deadline("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_DATE)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_deadline_past_input(self):
        self.initPage(ChangeOrderPage(self.driver))

        self.auth_client()
        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_deadline()
        self.page.fill_deadline(10101998)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_DATE)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_deadline_future_input(self):
        self.initPage(ChangeOrderPage(self.driver))
        self.auth_client()

        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_deadline()
        self.page.fill_deadline(10102998)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_FUTURE)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_empty_input(self):
        self.initPage(ChangeOrderPage(self.driver))
        self.auth_client()

        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_description()
        self.page.fill_discription("")
        self.page.select_category()
        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_long_input(self):
        self.initPage(ChangeOrderPage(self.driver))
        self.auth_client()

        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_description()
        self.page.fill_discription(
            "asdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkska"
        )
        self.page.select_category()
        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_cancel_button(self):
        self.initPage(ChangeOrderPage(self.driver))
        self.auth_client()

        self.page.open()
        self.page.waitOfVisible(self.CHANGE_BUTTON)
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        is_cancel = self.page.chek_cancel()
        self.assertEqual(is_cancel, True, f"Изменения не отменились")
