from steps.default import DefaultStep
from pages.ProfilePage import ProfilePage as Page


class ProfileStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def add_spec(self):
        self.page.add_spec()
        self.page.select_spec()

    def check_about_text(self):
        return self.page.get_about_text()

    def delete_spec(self):
        before = len(self.page.get_specs())
        self.page.delete_spec()
        after = len(self.page.get_specs())
        return before != after

    def check_exit(self):
        self.page.click_on_exit()
        return self.page.get_cookies()