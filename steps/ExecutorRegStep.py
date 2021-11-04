from steps.default import DefaultStep
from pages.ExecutorRegPage import ExecutorRegPage as Page


class ExecutorRegStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_error_select_spec(self):
        self.page.open()
        self.page.submit_spec()
        self.page.check_select_error()

    def check_success_select_spec(self):
        self.page.open()
        self.page.select_spec()
        select = self.page.check_selected_spec()
        self.page.submit_spec()
        self.page.wait_reg_page()
        return select
