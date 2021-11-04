from tests.default import DefaultTest
from steps.MainStep import MainStep


class MainTest(DefaultTest):
    def test_reg_spec(self):
        reg_step = MainStep(self.driver)
        is_ok = reg_step.check_redirect_spec()
        self.assertEqual(is_ok,
                         'Выберите специализацию',
                         'Вот и все, ребята'
                         )

    def test_reg_client(self):
            reg_step = MainStep(self.driver)
            is_ok = reg_step.check_redirect_client()
            self.assertEqual(is_ok,
                             'Регистрация за клиента',
                             'Вот и все, ребята'
                             )