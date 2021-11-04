from steps.SearchStep import SearchStep
from tests.default import DefaultTest


class SearchTest(DefaultTest):
    def test_select_suggest(self):
        self.auth_executor()

        searchStep = SearchStep(self.driver)
        isOk = searchStep.checkSelectAnySuggest()
        self.assertEqual(isOk,
                         True,
                         'Не удалось выбрать садджест'
                         )

    def test_search_with_filters(self):
        self.auth_executor()

        searchStep = SearchStep(self.driver)
        result = searchStep.checkSearchForFilters()
        self.assertEqual(len(result) > 0, True)

    def test_click_to_card_search_result(self):
        self.auth_executor()

        searchStep = SearchStep(self.driver)
        searchStep.checkClickToResultCardOrder()
        searchStep.checkClickToResultCardUser()
