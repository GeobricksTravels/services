import unittest
from core.dao_test import DAOTestCase
from core.utils_test import UtilsTestCase
from rest.dao_rest_test import DaoRestTest


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(UtilsTestCase))
    s.addTest(unittest.makeSuite(DAOTestCase))
    s.addTest(unittest.makeSuite(DaoRestTest))
    return s


my_suite = suite()
runner = unittest.TextTestRunner()
runner.run(my_suite)
