from selenium.webdriver import Keys

from steps.default import DefaultStep
from pages.SearchPage import SearchPage as Page


class SearchStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def checkSelectAnySuggest(self):
        self.page.open()
        self.page.fillSearch('t')
        self.page.fillSearch(Keys.BACKSPACE)
        suggest_text = self.page.selectFirstSuggest()
        search_text = self.page.getSearchValue()
        return suggest_text == search_text

    def checkSearchForFilters(self):
        filters = self.page.FILTERS

        self.page.open()
        self.page.fillClickableFilter(
            filters['searchFor'],
            filters['searchFor']['onlyUsers']
        )
        self.page.fillFilter(filters['from'], 0)
        self.page.fillFilter(filters['to'], 5)
        self.page.fillClickableFilter(
            filters['sort'],
            filters['sort']['rate']
        )
        self.page.fillClickableFilter(
            filters['desc'],
            filters['desc']['down']
        )

        self.page.submit()

        return self.page.getSearchResult()

    def checkClickToResultCardOrder(self):
        toOrder = [
            self.page.TITLE,
            self.page.MORE_DESCR
        ]
        toUser = [
            self.page.AVATAR,
        ]

        for item in toOrder:
            self.movesBeforeClick(item, 'onlyOrders')
            self.checkMoveToOrder()

        for item in toUser:
            self.movesBeforeClick(item, 'onlyOrders')
            self.checkMoveToUser()

    def checkClickToResultCardUser(self):
        self.movesBeforeClick(self.page.MORE_BTN_CATEGORY, 'onlyUsers')
        self.checkMoveToUser()

    def movesBeforeClick(self, xpath, only):
        filters = self.page.FILTERS
        self.page.open()
        self.page.fillClickableFilter(
            filters['searchFor'],
            filters['searchFor'][only]
        )
        self.page.submit()
        self.page.waitOfVisible(xpath)
        self.page.clickOnElement(xpath)

    def checkMoveToOrder(self):
        self.page.waitOfVisible(self.page.ORDER_PAGE)

    def checkMoveToUser(self):
        self.page.waitOfVisible(self.page.PROFILE_PAGE)
