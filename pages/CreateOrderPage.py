from pages.default import DefaultPage


class CreateOrderPage(DefaultPage):
    PATH = "/order-create"

    HEADER_INPUT = '//input[@name="order_name"]'
    BUDGET_INPUT = '//input[@name="budget"]'
    DEADLINE_INPUT = '//input[@name="date"]'
    CATEGORY = '//textarea[@name="category"]'
    CATEGORY_NAME = '//li[@data-id="2"]'
    SUBMIT = '//button[@id="send_mess"]'
    ORDER_CREATE_FORM = '//form[@id="order-create_form"]'
    DESCRIPTION = '//textarea[@name="description"]'

    ORDER_PAGE_TITLE = '//div[@class="orderPage__order_title"]'

    def fill_header(self, header):
        self.waitOfVisible(self.HEADER_INPUT)
        self.sendKeysOnElement(self.HEADER_INPUT, header)

    def fill_budget(self, budget):
        self.waitOfVisible(self.BUDGET_INPUT)
        self.sendKeysOnElement(self.BUDGET_INPUT, budget)

    def fill_deadline(self, deadline):
        self.waitOfVisible(self.DEADLINE_INPUT)
        self.sendKeysOnElement(self.DEADLINE_INPUT, deadline)

    def select_category(self):
        self.waitOfVisible(self.CATEGORY)
        self.clickOnElement(self.CATEGORY)
        self.waitOfVisible(self.CATEGORY_NAME)
        self.clickOnElement(self.CATEGORY_NAME)

    def fill_discription(self, desc):
        self.waitOfVisible(self.DESCRIPTION)
        self.sendKeysOnElement(self.DESCRIPTION, desc)

    def submit(self):
        self.waitOfVisible(self.SUBMIT)
        self.clickOnElement(self.SUBMIT)

    def wait_create_order_form(self):
        self.waitOfVisible(self.ORDER_CREATE_FORM)

    def check_error(self, err):
        return self.check_exists_by_xpath(err)

    def check_create_order(self):
        self.waitOfVisible(self.ORDER_PAGE_TITLE)
        return self.getTextFromElement(self.ORDER_PAGE_TITLE)
