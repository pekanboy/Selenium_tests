from tests.default import DefaultTest
from steps.ExecutorRegStep import ExecutorRegStep


class ExecutorRegTest(DefaultTest):
    def test_error_select_spec(self):
        step = ExecutorRegStep(self.driver)
        step.check_error_select_spec()

    def test_success_select_spec(self):
        step = ExecutorRegStep(self.driver)
        res = step.check_success_select_spec()
        self.assertEqual(
            len(res) > 0,
            True,
            'Не удалось выбрать специализацию'
        )
