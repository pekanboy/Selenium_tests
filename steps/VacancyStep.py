from steps.default import DefaultStep
from pages.VacancyPage import VacancyPage as Page


class VacancyStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_select_executor(self):
        self.page.open()
        return self.page.check_select_button()
    
    def check_cancel_executor(self):
        self.page.open()
        return self.page.check_cancel_button()

    def check_change_vacancy(self):
        self.page.open()
        return self.page.check_change_button()
    
    def check_end_vacancy(self):
        self.page.open()
        return self.page.check_end_button()

    def check_no_end_button(self):
        self.page.open()
        return self.page.check_no_end_button()

