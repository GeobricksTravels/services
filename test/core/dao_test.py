import unittest
from pymongo import Connection
from a_la_romana_services.core.dao import DAO


class DAOTestCase(unittest.TestCase):

    dao = None
    db_name = "a_la_romana_test_db"
    users = "test_users"
    activities = "test_activities"
    events = "test_events"
    config = {
        "db_name": db_name,
        "users": users,
        "activities": activities,
        "events": events
    }

    def setUp(self):
        self.dao = DAO(self.config)
        self.connection = Connection()
        self.connection.drop_database(self.db_name)
        self.connection.close()

    def tearDown(self):
        self.connection = Connection()
        self.connection.drop_database(self.db_name)
        self.connection.close()

    def test_setup(self):
        self.assertIsNotNone(self.dao)
        self.assertIsNotNone(self.dao.client)
        self.assertEquals(self.dao.db_name, self.db_name)
        self.assertEquals(self.dao.users, self.users)
        self.assertEquals(self.dao.activities, self.activities)
        self.assertEquals(self.dao.events, self.events)
        config = {}
        tmp = DAO(config)
        self.assertIsNotNone(tmp)
        self.assertIsNotNone(tmp.client)
        self.assertEquals(tmp.db_name, 'a_la_romana_db')
        self.assertEquals(tmp.users, 'users')
        self.assertEquals(tmp.activities, 'activities')
        self.assertEquals(tmp.events, 'events')

    def test_create_user(self):
        user = {"email": "someting@example.com"}
        user_id = self.dao.create_user(user)
        self.assertIsNotNone(user_id)
        user["id"] = user_id
        try:
            self.dao.create_user(user)
        except Exception, e:
            self.assertEquals(int(str(e)), 409)
        try:
            self.dao.create_user({})
        except Exception, e:
            self.assertEquals(int(str(e)), 400)
        user = {
            "_id": "507f191e810c19729de860ea",
            "email": "someting@example.com"
        }
        self.dao.create_user(user)

    def tes_get_user(self):
        u = self.dao.get_user('507f191e810c19729de860ea')
        self.assertIsNone(u)
        u = self.dao.get_user(None)
        self.assertEquals(u.count(), 0)
