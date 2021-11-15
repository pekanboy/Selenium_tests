from tests.default import DefaultTest
from pages.NavbarsPage import NavbarsPage as Page


class NavbarsTest(DefaultTest):
    def test_vacancy(self):
        self.initPage(Page(self.driver))
        self.auth_client()
        self.page.open()
        self.page.click_vacancy_button()
        self.page.wait_vacancy()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_order(self):
        self.initPage(Page(self.driver))
        self.auth_client()
        self.page.open()
        self.page.click_order_button()
        self.page.wait_order()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_logo(self):
        self.initPage(Page(self.driver))
        self.auth_client()
        self.page.open()
        self.page.click_logo()
        self.page.wait_logo()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_person(self):
        self.initPage(Page(self.driver))
        self.auth_client()
        self.page.open()
        self.page.click_person()
        self.page.wait_person()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_loop(self):
        self.initPage(Page(self.driver))
        self.auth_client()
        self.page.open()
        self.page.click_loop()
        self.page.wait_loop()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_vacancies_spec(self):
        self.initPage(Page(self.driver))
        self.auth_executor()
        self.page.open()
        self.page.click_vacancies_spec()
        self.page.wait_vacancies_spec()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_orders_spec(self):
        self.initPage(Page(self.driver))
        self.auth_executor()
        self.page.open()
        self.page.click_orders_spec()
        self.page.wait_orders_spec()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_reg_client(self):
        self.initPage(Page(self.driver))
        self.page.open()
        self.page.click_reg()
        self.page.click_reg_client()
        self.page.wait_reg_client()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_reg_spec(self):
        self.initPage(Page(self.driver))
        self.page.open()
        self.page.click_reg()
        self.page.click_reg_spec()
        self.page.wait_reg_spec()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")

    def test_reg_login(self):
        self.initPage(Page(self.driver))
        self.page.open()
        self.page.click_login()
        self.page.wait_login()
        is_ok = True
        self.assertEqual(is_ok, True, "Вот и все, ребята")
