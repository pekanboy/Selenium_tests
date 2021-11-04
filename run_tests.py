import sys
import unittest

from tests.AllOrdersStep import AllOrdersTest
from tests.AuthTest import AuthTest
from tests.SearchTest import SearchTest
from tests.ExecutorRegTest import ExecutorRegTest
from tests.ClientRegTest import ClientRegTest
from tests.ProfileTest import ProfileTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(AllOrdersTest),
        unittest.makeSuite(ExecutorRegTest),
        unittest.makeSuite(ClientRegTest),
        unittest.makeSuite(ProfileTest)
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
