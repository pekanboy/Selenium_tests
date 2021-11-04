import sys
import unittest

from tests.AllOrdersStep import AllOrdersTest
from tests.AuthTest import AuthTest
from tests.ChangeOrderTest import ChangeOrderTest
from tests.ChangeVacancyTest import ChangeVacancyrTest
from tests.CreateVacancyTest import CreateVacancyTest
from tests.SearchTest import SearchTest
from tests.CreateOrderTest import CreateOrderTest
from tests.OrderTest import OrderTest
from tests.VacancyTest import VacancyTest 

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(AllOrdersTest),
        unittest.makeSuite(CreateOrderTest),
        unittest.makeSuite(OrderTest),
        unittest.makeSuite(ChangeOrderTest),
        unittest.makeSuite(CreateVacancyTest),
        unittest.makeSuite(VacancyTest),
        unittest.makeSuite(ChangeVacancyrTest),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
