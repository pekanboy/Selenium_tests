from pages.default import DefaultPage


class OrderPage(DefaultPage):
    PATH = '/order/19'

    SELECT_BUTTON = '//button[@data-id="58"]'
    CANCEL_BUTTON = '//button[@class="orderPage__set-rate_button-exit"]'
    CHANGE_BUTTON = '//button[@class="vacancyPage__customer-button_change"]'
    END_BUTTON = '//button[@class="orderPage__order_end"]'
    NO_END_BUTTON = '//button[@class="mini-button__elem_no"]'

    SELECT_EXECUTOR = '//div[@class="orderPage__set-rate"]'
    SETTINGS_WINDOW = '//form[@id="order-create_form"]'
    END_WINDOW = '//div[@class="orderPage__feedback_window"]'

    ORDER_PAGE_TITLE = '//div[@class="orderPage__order_title"]'
    SELECT_TEXT = "//*[contains(text(), 'Выбранный исполнитель')]"

    def check_select_button(self ):
        self.waitOfVisible(self.SELECT_BUTTON)
        self.clickOnElement(self.SELECT_BUTTON)
        self.waitOfVisible(self.SELECT_TEXT)
        is_select = self.check_exists_by_xpath(self.SELECT_EXECUTOR)
        if is_select:
            self.clickOnElement(self.CANCEL_BUTTON)
        return is_select

    def check_cancel_button(self ):
        self.waitOfVisible(self.SELECT_BUTTON)
        self.clickOnElement(self.SELECT_BUTTON)
        self.waitOfVisible(self.CANCEL_BUTTON)
        self.clickOnElement(self.CANCEL_BUTTON)
        self.waitOfVisible(self.SELECT_BUTTON)
        is_select = self.check_exists_by_xpath(self.SELECT_BUTTON)
        return is_select

    def check_change_button(self):
        self.waitOfVisible(self.CHANGE_BUTTON)
        self.clickOnElement(self.CHANGE_BUTTON)
        return self.check_exists_by_xpath(self.SETTINGS_WINDOW)

    def check_end_button(self):
        self.waitOfVisible(self.SELECT_BUTTON)
        self.clickOnElement(self.SELECT_BUTTON)
        self.waitOfVisible(self.END_BUTTON)
        self.clickOnElement(self.END_BUTTON)
        self.waitOfVisible(self.END_WINDOW)
        is_window = self.check_exists_by_xpath(self.END_WINDOW)
        if is_window:
            self.waitOfVisible(self.NO_END_BUTTON)
            self.clickOnElement(self.NO_END_BUTTON)
            self.waitOfVisible(self.CANCEL_BUTTON)
            self.clickOnElement(self.CANCEL_BUTTON)
        return is_window

    def check_no_end_button(self):
        self.waitOfVisible(self.SELECT_BUTTON)
        self.clickOnElement(self.SELECT_BUTTON)
        self.waitOfVisible(self.END_BUTTON)
        self.clickOnElement(self.END_BUTTON)
        self.waitOfVisible(self.NO_END_BUTTON)
        self.clickOnElement(self.NO_END_BUTTON)
        self.waitOfVisible(self.ORDER_PAGE_TITLE)
        is_order = self.check_exists_by_xpath(self.ORDER_PAGE_TITLE)
        if is_order: 
            self.waitOfVisible(self.CANCEL_BUTTON)
            self.clickOnElement(self.CANCEL_BUTTON)
        return self.check_exists_by_xpath(self.ORDER_PAGE_TITLE)
