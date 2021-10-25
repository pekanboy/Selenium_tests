from steps.SearchStep import SearchStep
from tests.default import DefaultTest


class SearchTest(DefaultTest):
    def test_select_suggest(self):
        self.auth()

        searchStep = SearchStep(self.driver)
        isOk = searchStep.checkSelectAnySuggest()

        self.assertEqual(isOk,
                         True,
                         'Не удалось выбрать садджест'
        )

    def test_search_with_filters(self):
        self.auth()

        searchStep = SearchStep(self.driver)
        result = searchStep.checkSearchForFilters()
        self.assertEqual(len(result) > 0, True)
