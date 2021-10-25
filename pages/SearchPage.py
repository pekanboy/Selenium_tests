from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.default import DefaultPage


class SearchPage(DefaultPage):
    PATH = '/search'
    FILTERS = {
        'searchFor': {
            'this': '//textarea[@name="what"]',
            'onlyUsers': '//*[@data-id=43]',
            'onlyOrders': '//*[@data-id=41]',
            'onlyVacancies': '//*[@data-id=42]'
        },
        'from': '//input[@name="salaryFrom"]',
        'to': '//input[@name="salaryTo"]',
        'sort': {
            'this': '//textarea[@name="sort"]',
            'rate': '//li[contains(text(),"Рейтингу")]',
        },
        'desc': {
            'this': '//textarea[@name="desc"]',
            'down': '//li[contains(text(),"Уменьшению")]',
            'up': '//li[contains(text(),"Возрастанию")]',
        },
        'category': {
            'this': '//textarea[@name="category"]',
            'finance': '//li[contains(text(),"Финансовое планирование")]'
        }
    }
    SEARCH = '//input[@name="search"]'
    FIND = '//button[contains(text(),"Найти")]'
    SUGGEST = '//div[contains(@class, "suggest")]'
    RESULTS = '//div[@class="orders__order"]'

    def fillSearch(self, value):
        self.driver.find_element_by_xpath(self.SEARCH).click()
        self.driver.find_element_by_xpath(self.SEARCH).send_keys(value)

    def selectFirstSuggest(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: expected_conditions.visibility_of(d.find_element_by_xpath(self.SUGGEST))
        )

        suggest_text = self.driver.find_element_by_xpath(self.SUGGEST).text
        self.driver.find_element_by_xpath(self.SUGGEST).click()

        return suggest_text

    def getSearchValue(self):
        return self.driver.find_element_by_xpath(self.SEARCH).get_property("value")

    def fillClickableFilter(self, parent, child):
        self.driver.find_element_by_xpath(parent['this']).click()
        self.driver.find_element_by_xpath(child).click()

    def fillFilter(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def find(self):
        self.driver.find_element_by_xpath(self.FIND).click()

    def getSearchResult(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: expected_conditions.visibility_of(d.find_element_by_xpath(self.RESULTS))
        )

        return self.driver.find_elements_by_xpath(self.RESULTS)
