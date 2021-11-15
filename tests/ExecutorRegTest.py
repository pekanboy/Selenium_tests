from tests.default import DefaultTest
from pages.ExecutorRegPage import ExecutorRegPage as Page


class ExecutorRegTest(DefaultTest):
    def test_error_select_spec(self):
        self.initPage(Page(self.driver))

        self.page.open()
        self.page.submit_spec()
        self.page.check_select_error()

    def test_success_select_spec(self):
        self.initPage(Page(self.driver))

        self.page.open()
        self.page.select_spec()
        select = self.page.check_selected_spec()
        self.page.submit_spec()
        self.page.wait_reg_page()

        self.assertEqual(
            len(select) > 0,
            True,
            'Не удалось выбрать специализацию'
        )
