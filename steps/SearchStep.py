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

        self.page.fillSearch('')
        self.page.find()

        return self.page.getSearchResult()
