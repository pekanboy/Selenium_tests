from pages.CreateVacancyPage import CreateVacancyPage
from tests.default import DefaultTest


class CreateVacancyTest(DefaultTest):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_SUMM = "//*[contains(text(), 'Недопустимая сумма')]"

    def test_create_vacancy(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        vacancy_name = "хочу питсы"
        vacancy_budget = 228
        descrioption = "закажите мне питсы"

        self.page.open()
        self.page.fill_header(vacancy_name)
        self.page.fill_budget(vacancy_budget)
        self.page.select_category()
        self.page.fill_discription(descrioption)
        self.page.submit()

        real_vacancy = self.page.check_create_vacancy()
        self.assertEqual(
            real_vacancy,
            vacancy_name,
            f"Создать заказ не удалось:  имя заказа ${real_vacancy} "
            f"не совпадает с ожидаемым ${vacancy_name}",
        )

    def test_empty_header_input(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_header("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_long_header_input(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_header(
            "asfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыа"
        )
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_empty_input(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_budget("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_budget_long_input(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_budget(123123123123123)
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_SUMM)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_empty_input(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_discription("")
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")

    def test_descritiopn_long_input(self):
        self.initPage(CreateVacancyPage(self.driver))
        self.auth_client()
        self.page.open()
        self.page.fill_discription(
            "asdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkska"
        )
        self.page.select_category()

        is_err = self.page.check_error(self.ERR_LENGTH)
        self.assertEqual(is_err, True, f"Ошибка инпута не появилась")
