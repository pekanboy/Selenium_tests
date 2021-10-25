from pages.default import DefaultPage


class AllOrdersPage(DefaultPage):
    PATH = '/orders'

    AVATAR = '//img[@class="orders__order_img"]'
    TITLE = '//a[@class="orders__order_title"]'
    MORE_DESCR = '//a[contains(text(),"...показать еще")]'

    ORDER_PAGE = '//div[@class="orderPage"]'
    PROFILE_PAGE = '//div[@class="profile"]'
