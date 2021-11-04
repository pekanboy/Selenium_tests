from steps.default import DefaultStep
from pages.ChangeVacancyPage import ChangeVacancyPage as Page
import random
import string


class ChangeVacancyStep(DefaultStep):
    ERR_LENGTH = "//*[contains(text(), 'Недопустимая длина')]"
    ERR_SUMM = "//*[contains(text(), 'Недопустимая сумма')]"
    ERR_DATE = "//*[contains(text(), 'Некорректная дата')]"
    ERR_FUTURE = "//*[contains(text(), 'Вряд ли вы столько проживёте...')]"
    CHANGE_BUTTON = '//button[@class="vacancyPage__customer-button_change"]'

    SETTINGS_LABEL = '//div[@class="settings__label"]'

    def __init__(self, driver):
        super().__init__(Page(driver))

    def check_change_vacancy(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(10))
        vacancy_name = 'хочу многа питсы' + result_str
        vacancy_budget = 228
        descrioption = 'закажите мне питсы но теперь побольше'

        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)

        self.page.clear_header()
        self.page.clear_budget()
        self.page.clear_description()

        self.page.fill_header(vacancy_name)
        self.page.fill_budget(vacancy_budget)
        self.page.select_category()
        self.page.fill_discription(descrioption)
        self.page.submit()
        return (vacancy_name, self.page.check_change_vacancy())
    
    def check_header_empty_input(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_header()
        self.page.fill_header('')
        self.page.select_category()
        return self.page.check_error(self.ERR_LENGTH)

    def check_header_long_input(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_header()
        self.page.fill_header('asfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыаasfsыа')
        self.page.select_category()
        return self.page.check_error(self.ERR_LENGTH)
    
    def check_budget_empty_input(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_budget()
        self.page.fill_budget('')
        self.page.select_category()
        return self.page.check_error(self.ERR_SUMM)

    def check_budget_long_input(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_budget()
        self.page.fill_budget(123123123123123)
        self.page.select_category()
        return self.page.check_error(self.ERR_SUMM)


    def check_description_empty_input(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_description()
        self.page.fill_discription('')
        self.page.select_category()
        return self.page.check_error(self.ERR_LENGTH)
    
    def check_description_long_input(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        self.page.clear_description()
        self.page.fill_discription('asdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkskaasdfkfkska')
        self.page.select_category()
        return self.page.check_error(self.ERR_LENGTH)
    
    def check_cancel_button(self):
        self.page.open()
        self.page.clickOnElement(self.CHANGE_BUTTON)
        self.page.waitOfVisible(self.SETTINGS_LABEL)
        return self.page.chek_cancel()
