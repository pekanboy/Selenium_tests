from pages.default import DefaultPage


class ExecutorRegPage(DefaultPage):
    PATH = "/add-spec"

    SELECT_SPEC = '//*[@name="category"]'
    SELECT_SPEC_ERR = '//*[@class="select__input form-control_error"]'
    SPEC = '//*[contains(text(),"Финансовое планирование")]'
    SPEC_SUBMIT = '//*[@id="send_mess"]'

    REG_FORM = '//*[@class="registration"]'

    def select_spec(self):
        self.clickOnElement(self.SELECT_SPEC)
        self.clickOnElement(self.SPEC)
        return self.getTextFromElement(self.SELECT_SPEC)

    def submit_spec(self):
        self.clickOnElement(self.SPEC_SUBMIT)

    def wait_reg_page(self):
        self.waitOfVisible(self.REG_FORM)

    def check_selected_spec(self):
        return self.getTextFromElement(self.SELECT_SPEC)

    def check_select_error(self):
        self.waitOfVisible(self.SELECT_SPEC_ERR)
