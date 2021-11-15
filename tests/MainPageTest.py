from tests.default import DefaultTest
from pages.MainPage import MainPage as Page


class MainPageTest(DefaultTest):
    def test_reg_spec(self):
        self.initPage(Page(self.driver))
        self.page.open()
        self.page.click_spec()
        self.page.wait_registration_spec()
        is_ok = self.page.get_reg_spec()
        self.assertEqual(is_ok, "Выберите специализацию", "Вот и все, ребята")

    def test_reg_client(self):
        self.initPage(Page(self.driver))
        self.page.open()
        self.page.open()
        self.page.click_client()
        self.page.wait_registration_client()
        is_ok = self.page.get_reg_client()
        self.assertEqual(is_ok, "Регистрация за клиента", "Вот и все, ребята")
