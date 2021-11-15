from pages.VacancyPage import VacancyPage
from tests.default import DefaultTest


class VacancyTest(DefaultTest):
    def test_select_executor(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()

        self.page.open()
        is_select = self.page.check_select_button()
        self.assertEqual(is_select, True, f"Исполнитель не выбрался")

    def test_cancel_executor(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()

        self.page.open()
        is_cancel = self.page.check_cancel_button()
        self.assertEqual(is_cancel, True, f"Не получилось отказатсья от исполнителя")

    def test_change_vacancy_window(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()

        self.page.open()
        is_open = self.page.check_change_button()
        self.assertEqual(is_open, True, f"Окно изменения заказа не открылось")

    def test_end_vacancy(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()

        is_open = self.page.check_end_button()
        self.assertEqual(
            is_open, True, f"Окно подтверждения завершения заказа не появилось"
        )

    def test_no_end_button(self):
        self.initPage(VacancyPage(self.driver))
        self.auth_client()
        self.page.open()

        is_close = self.page.check_no_end_button()
        self.assertEqual(
            is_close, True, f"Окно подтверджения завершения заказа не закрылось"
        )
