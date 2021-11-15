from pages.default import DefaultPage


class VacancyPage(DefaultPage):
    PATH = 'vacancy/6'

    SELECT_BUTTON = '//button[@data-id="66"]'
    CANCEL_BUTTON = '//button[@class="vacancyPage__comment-button_cancel"]'
    CHANGE_BUTTON = '//button[@class="vacancyPage__customer-button_change"]'
    END_BUTTON = '//button[@class="orderPage__order_end"]'
    NO_END_BUTTON = '//button[@class="mini-button__elem_no"]'

    SETTINGS_WINDOW = '//form[@id="order-create_form"]'
    END_WINDOW = '//div[@class="orderPage__feedback_window"]'

    VACANCY_PAGE_TITLE = '//div[@class="orderPage__order_title"]'
    SELECT_TEXT = "//*[contains(text(), 'Связаться')]"

    def check_select_button(self):
        self.clickOnElement(self.SELECT_BUTTON)
        is_select = self.check_exists_by_xpath(self.SELECT_TEXT)
        if is_select:
            self.clickOnElement(self.CANCEL_BUTTON)
        return is_select

    def check_cancel_button(self):
        self.clickOnElement(self.SELECT_BUTTON)
        self.clickOnElement(self.CANCEL_BUTTON)
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
        self.waitOfVisible(self.VACANCY_PAGE_TITLE)
        is_vacancy = self.check_exists_by_xpath(self.VACANCY_PAGE_TITLE)
        if is_vacancy: 
            self.waitOfVisible(self.CANCEL_BUTTON)
            self.clickOnElement(self.CANCEL_BUTTON)
        return self.check_exists_by_xpath(self.VACANCY_PAGE_TITLE)
