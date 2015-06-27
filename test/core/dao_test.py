import unittest
from a_la_romana_services.core.dao import DAO


class DAOTestCase(unittest.TestCase):

    dao = None
    config = {
        "db_name": "a_la_romana_test_db",
        "users": "test_users",
        "activities": "test_activities",
        "events": "test_events"
    }

    def setUp(self):
        self.dao = DAO(self.config)

    def test_setup(self):
        self.assertIsNotNone(self.dao)
