from tests.default import DefaultTest
from steps.NavbarsStep import NavbarsStep


class NavbarsTest(DefaultTest):
    def test_vacancy(self):
        self.auth_client()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_vacancy()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_order(self):
        self.auth_client()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_order()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_logo(self):
        self.auth_client()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_logo()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_person(self):
        self.auth_client()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_person()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_loop(self):
        self.auth_client()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_loop()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_vacancies_spec(self):
        self.auth_executor()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_vacancies_spec()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_orders_spec(self):
        self.auth_executor()
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_orders_spec()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_reg_client(self):
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_reg_client()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_reg_spec(self):
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_reg_client()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )

    def test_reg_login(self):
        reg_step = NavbarsStep(self.driver)
        is_ok = reg_step.check_redirect_login()
        self.assertEqual(is_ok,
                         True,
                         'Вот и все, ребята'
                         )