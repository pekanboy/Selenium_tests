from pages.VacancyPage import VacancyPage
from tests.default import DefaultTest
import random
import string


class ChangeVacancyrTest(DefaultTest):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_SUMM = "//*[contains(text(), 'Недопустимая сумма')]"
    ERR_DATE = "//*[contains(text(), 'Некорректная дата')]"
    ERR_FUTURE = "//*[contains(text(), 'Вряд ли вы столько проживёте...')]"
    CHANGE_BUTTON = '//button[@class="vacancyPage__customer-button_change"]'

    SETTINGS_LABEL = '//div[@class="settings__label"]'

    def test_change_vacancy(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()

        letters = string.ascii_lowercase
        result_str = "".join(random.choice(letters) for i in range(10))
        vacancy_name = "хочу многа питсы" + result_str
        vacancy_budget = 228
        descrioption = "закажите мне питсы но теперь побольше"

        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)

        self.page.clear_header()
        self.page.clear_budget()
        self.page.clear_description()

        self.page.fill_header(vacancy_name)
        self.page.fill_budget(vacancy_budget)
        self.page.select_category()
        self.page.fill_discription(descrioption)
        self.page.submit()

        real_vacancy = self.page.check_change_vacancy()
        self.assertEqual(
            real_vacancy,
            vacancy_name,
            f"Изменить заказ не удалось:  имя заказа ${real_vacancy} "
            f"не совпадает с ожидаемым ${vacancy_name}",
        )

    def test_empty_header_input(self):
        self.initPage(VacancyPage(self.driver))
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
        self.initPage(VacancyPage(self.driver))
        self.auth_client()

        self.page.open()
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
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_budget()
        self.page.fill_budget("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_long_input(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_budget()
        self.page.fill_budget(123123123123123)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_empty_input(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_description()
        self.page.fill_discription("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_long_input(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()
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
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)

        is_cancel = self.page.chek_cancel()
        self.assertEqual(is_cancel, True, f"Изменения не отменились")
