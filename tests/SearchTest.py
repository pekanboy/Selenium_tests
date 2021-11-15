from selenium.webdriver import Keys

from tests.default import DefaultTest
from pages.SearchPage import SearchPage as Page


class SearchTest(DefaultTest):
    def test_select_suggest(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        self.page.open()
        self.page.fillSearch("t")
        self.page.fillSearch(Keys.BACKSPACE)
        suggest_text = self.page.selectFirstSuggest()
        search_text = self.page.getSearchValue()

        self.assertEqual(suggest_text, search_text, "Не удалось выбрать садджест")

    def test_search_with_filters(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        filters = self.page.FILTERS

        self.page.open()
        self.page.fillClickableFilter(
            filters["searchFor"], filters["searchFor"]["onlyUsers"]
        )
        self.page.fillFilter(filters["from"], 0)
        self.page.fillFilter(filters["to"], 5)
        self.page.fillClickableFilter(filters["sort"], filters["sort"]["rate"])
        self.page.fillClickableFilter(filters["desc"], filters["desc"]["down"])

        self.page.submit()

        result = self.page.getSearchResult()
        self.assertEqual(len(result) > 0, True)

    def test_click_to_card_search_result(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        toOrder = [
            self.page.TITLE,
        ]
        toUser = [
            self.page.AVATAR,
        ]

        for item in toOrder:
            self.movesBeforeClick(item, "onlyOrders")
            self.checkMoveToOrder()

        for item in toUser:
            self.movesBeforeClick(item, "onlyOrders")
            self.checkMoveToUser()

        self.movesBeforeClick(self.page.MORE_BTN_CATEGORY, "onlyUsers")
        self.checkMoveToUser()

    def movesBeforeClick(self, xpath, only):
        filters = self.page.FILTERS
        self.page.open()
        self.page.fillClickableFilter(filters["searchFor"], filters["searchFor"][only])
        self.page.submit()
        self.page.clickOnElement(xpath)

    def checkMoveToOrder(self):
        self.page.waitOfVisible(self.page.ORDER_PAGE)

    def checkMoveToUser(self):
        self.page.waitOfVisible(self.page.PROFILE_PAGE)
