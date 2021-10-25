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
    AVATAR = '//img[@class="orders__order_img"]'
    TITLE = '//a[@class="orders__order_title"]'
    MORE_DESCR = '//a[contains(text(),"...показать еще")]'
    MORE_BTN_CATEGORY = '//button[contains(text(),"ещё...")]'

    ORDER_PAGE = '//div[@class="orderPage"]'
    PROFILE_PAGE = '//div[@class="profile"]'

    def fillSearch(self, value):
        self.clickOnElement(self.SEARCH)
        self.sendKeysOnElement(self.SEARCH, value)

    def selectFirstSuggest(self):
        self.waitOfVisible(self.SUGGEST)
        suggest_text = self.getTextFromElement(self.SUGGEST)
        self.clickOnElement(self.SUGGEST)

        return suggest_text

    def getSearchValue(self):
        return self.driver.find_element_by_xpath(self.SEARCH).get_property("value")

    def fillClickableFilter(self, parent, child):
        self.clickOnElement(parent['this'])
        self.clickOnElement(child)

    def fillFilter(self, xpath, value):
        self.clickOnElement(xpath)
        self.sendKeysOnElement(xpath, value)

    def submit(self):
        self.clickOnElement(self.FIND)

    def getSearchResult(self):
        self.waitOfVisible(self.RESULTS)
        return self.driver.find_elements_by_xpath(self.RESULTS)
