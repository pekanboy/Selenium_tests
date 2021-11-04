from steps.AllOrdersStep import AllOrdersStep
from tests.default import DefaultTest


class AllOrdersTest(DefaultTest):
    def test_clickable_fields_in_result_card(self):
        self.auth_client()

        step = AllOrdersStep(self.driver)
        step.checkClickToResultCard()
