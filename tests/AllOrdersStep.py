from tests.default import DefaultTest
from pages.AllOrdersPage import AllOrdersPage as Page


class AllOrdersTest(DefaultTest):
    def test_clickable_fields_in_result_card(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        toOrder = [self.page.TITLE, self.page.MORE_DESCR]
        toUser = [
            self.page.AVATAR,
        ]

        for item in toOrder:
            self.page.open()
            self.page.waitOfVisible(item)
            self.page.clickOnElement(item)
            self.checkMoveToOrder()

        for item in toUser:
            self.page.open()
            self.page.waitOfVisible(item)
            self.page.clickOnElement(item)
            self.checkMoveToUser()

    def checkMoveToOrder(self):
        self.page.waitOfVisible(self.page.ORDER_PAGE)

    def checkMoveToUser(self):
        self.page.waitOfVisible(self.page.PROFILE_PAGE)
