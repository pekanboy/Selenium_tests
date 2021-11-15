from pages.default import DefaultPage


class ChangeOrderPage(DefaultPage):
    PATH = "/order/19"

    HEADER_INPUT = '//input[@name="order_name"]'
    BUDGET_INPUT = '//input[@name="budget"]'
    DEADLINE_INPUT = '//input[@name="date"]'
    CATEGORY = '//textarea[@name="category"]'
    CATEGORY_NAME = '//li[@data-id="2"]'
    SUBMIT = '//button[@id="send_mess"]'
    ORDER_CREATE_FORM = '//form[@id="order-create_form"]'
    DESCRIPTION = '//textarea[@name="description"]'

    ORDER_PAGE_TITLE = '//div[@class="orderPage__order_title"]'

    CANCEL_BUTTON = '//button[@class="change-form__cancel"]'

    def clear_header(self):
        self.clear_field(self.HEADER_INPUT)

    def clear_budget(self):
        self.clear_field(self.BUDGET_INPUT)

    def clear_deadline(self):
        self.clear_field(self.DEADLINE_INPUT)

    def clear_description(self):
        self.clear_field(self.DESCRIPTION)

    def fill_header(self, header):
        self.sendKeysOnElement(self.HEADER_INPUT, header)

    def fill_budget(self, budget):
        self.sendKeysOnElement(self.BUDGET_INPUT, budget)

    def fill_deadline(self, deadline):
        self.sendKeysOnElement(self.DEADLINE_INPUT, deadline)

    def select_category(self):
        self.clickOnElement(self.CATEGORY)
        self.waitOfVisible(self.CATEGORY_NAME)
        self.clickOnElement(self.CATEGORY_NAME)

    def fill_discription(self, desc):
        self.sendKeysOnElement(self.DESCRIPTION, desc)

    def submit(self):
        self.clickOnElement(self.SUBMIT)

    def wait_create_order_form(self):
        self.waitOfVisible(self.ORDER_CREATE_FORM)

    def check_error(self, err):
        return self.check_exists_by_xpath(err)

    def chek_cancel(self):
        self.clickOnElement(self.CANCEL_BUTTON)
        self.waitOfVisible(self.ORDER_PAGE_TITLE)
        return self.check_exists_by_xpath(self.ORDER_PAGE_TITLE)

    def check_change_order(self):
        self.waitOfVisible(self.ORDER_PAGE_TITLE)
        return self.getTextFromElement(self.ORDER_PAGE_TITLE)
