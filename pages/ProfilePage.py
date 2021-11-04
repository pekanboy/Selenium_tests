from pages.default import DefaultPage


class ProfilePage(DefaultPage):
    ABOUT = '//div[@class="about-text"]'
    EXIT = '//button[@class="exit-buttion__text"]'
    ADD_SPEC = '//div[@class="add-spec__text"]'
    SPEC_ITEM = '//div[@class="specializes__name"]'
    DELETE_SPEC = '//*[@class="specializes__close"]'

    ADD_SELECT_SPEC = '//*[@name="category"]'
    SPEC = '//*[contains(text(),"Финансовое планирование")]'
    ADD_SPEC_SUBMIT = '//*[@id="send_mess"]'

    SELECT_SPEC = '//*[@name="category"]'

    def click_on_exit(self):
        self.clickOnElement(self.EXIT)

    def get_about_text(self):
        return self.getTextFromElement(self.ABOUT)

    def delete_spec(self):
        self.clickOnElement(self.DELETE_SPEC)

    def get_specs(self):
        return self.driver.find_elements_by_xpath(self.SPEC_ITEM)

    def add_spec(self):
        self.clickOnElement(self.ADD_SPEC)

    def select_spec(self):
        self.clickOnElement(self.ADD_SELECT_SPEC)
        self.clickOnElement(self.SPEC)
        self.clickOnElement(self.ADD_SPEC_SUBMIT)