from steps.default import DefaultStep
from pages.AllOrdersPage import AllOrdersPage as Page


class AllOrdersStep(DefaultStep):
    def __init__(self, driver):
        super().__init__(Page(driver))

    def checkClickToResultCard(self):
        toOrder = [
            self.page.TITLE,
            self.page.MORE_DESCR
        ]
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