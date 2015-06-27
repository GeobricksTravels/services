import unittest
from a_la_romana_services.core import utils


class UtilsTestCase(unittest.TestCase):

    def test_is_valid_user(self):
        user = {"email": "something@test.com"}
        self.assertEquals(utils.is_valid_user(user), True)
        user = {}
        self.assertEquals(utils.is_valid_user(user), False)
