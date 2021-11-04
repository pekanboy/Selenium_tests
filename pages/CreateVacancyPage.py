from pages.default import DefaultPage


class CreateVacancyPage(DefaultPage):
    PATH = '/vacancy-create'

    HEADER_INPUT = '//input[@name="order_name"]'
    BUDGET_INPUT = '//input[@name="budget"]'
    CATEGORY = '//textarea[@name="category"]'
    CATEGORY_NAME = '//li[@data-id="2"]'
    SUBMIT = '//button[@id="send_mess"]'
    VACANCY_CREATE_FORM = '//form[@id="order-create_form"]'
    DESCRIPTION =  '//textarea[@name="description"]'

    VACANCY_PAGE_TITLE = '//div[@class="orderPage__order_title"]'

    def fill_header(self, header):
        self.sendKeysOnElement(self.HEADER_INPUT, header)

    def fill_budget(self, budget):
        self.sendKeysOnElement(self.BUDGET_INPUT, budget)

    def select_category(self):
        self.clickOnElement(self.CATEGORY)
        self.waitOfVisible(self.CATEGORY_NAME)
        self.clickOnElement(self.CATEGORY_NAME)

    def fill_discription(self, desc):
        self.sendKeysOnElement(self.DESCRIPTION, desc)
    
    def submit(self):
        self.clickOnElement(self.SUBMIT)

    def wait_create_vacancy_form(self):
        self.waitOfVisible(self.VACANCY_CREATE_FORM)

    def check_error(self, err):
        return self.check_exists_by_xpath(err)

    def check_create_vacancy(self):
        self.waitOfVisible(self.VACANCY_PAGE_TITLE)
        return self.getTextFromElement(self.VACANCY_PAGE_TITLE)
