import sys
import unittest

from tests.AllOrdersStep import AllOrdersTest
from tests.AuthTest import AuthTest
from tests.SearchTest import SearchTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(AllOrdersTest),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
