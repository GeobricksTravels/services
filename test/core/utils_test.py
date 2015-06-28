import unittest
from a_la_romana_services.core import utils


class UtilsTestCase(unittest.TestCase):

    def test_is_valid_user(self):
        user = {
            "user_id": "12345678",
            "name": "John Doe",
            "email": "something@test.com",
            "image_url": "http://www.test.com/imege.jpg"
        }
        self.assertEquals(utils.is_valid_user(user), True)
        user = {}
        self.assertEquals(utils.is_valid_user(user), False)
