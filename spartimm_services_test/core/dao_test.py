import unittest
from pymongo import MongoClient
from spartimm_services.core.dao import DAO
from spartimm_services.core.utils import clean_test_db
from spartimm_services.config import settings as s


class DAOTestCase(unittest.TestCase):

    dao = None
    config = s.test_config
    db_name = s.test_db_name

    def setUp(self):
        self.dao = DAO(self.config)
        self.client = MongoClient()
        self.db = self.client[self.db_name]
        clean_test_db()

    def tearDown(self):
        clean_test_db()

    def test_setup(self):
        self.assertIsNotNone(self.dao)
        self.assertIsNotNone(self.dao.client)
        self.assertEquals(self.dao.db_name, self.db_name)
        self.assertEquals(self.dao.users, self.config["users"])
        self.assertEquals(self.dao.activities, self.config["activities"])
        self.assertEquals(self.dao.events, self.config["events"])
        config = {}
        tmp = DAO(config)
        self.assertIsNotNone(tmp)
        self.assertIsNotNone(tmp.client)
        self.assertEquals(tmp.db_name, s.db_name)
        self.assertEquals(tmp.users, s.users)
        self.assertEquals(tmp.activities, s.activities)
        self.assertEquals(tmp.events, s.events)

    def test_create_user(self):
        user = {
            "user_id": "12345678",
            "name": "John Doe",
            "email": "something@test.com",
            "image_url": "http://www.test.com/imege.jpg"
        }
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
            "user_id": "12345678",
            "name": "John Doe",
            "image_url": "http://www.test.com/imege.jpg",
            "email": "someting@example.com"
        }
        try:
            self.dao.create_user(user)
        except Exception, e:
            self.assertEquals(int(str(e)), 409)

    def test_get_user(self):
        u = self.dao.get_user('507f191e810c19729de860ea')
        self.assertIsNone(u)
        u = self.dao.get_user(None)
        self.assertEquals(u.count(), 0)

    def test_delete_user(self):
        user = {
            "user_id": "12345678",
            "name": "John Doe",
            "email": "something@test.com",
            "image_url": "http://www.test.com/imege.jpg"
        }
        user_id = self.dao.create_user(user)
        self.assertIsNotNone(user_id)
        out = self.dao.delete_user(user['user_id'])
        self.assertEquals(out['ok'], 1)
        try:
            self.dao.delete_user(user['user_id'])
        except Exception, e:
            self.assertEquals(int(str(e)), 404)

    def test_update_user(self):
        user = {
            "user_id": "12345678",
            "name": "John Doe",
            "email": "something@test.com",
            "image_url": "http://www.test.com/imege.jpg"
        }
        user_id = self.dao.create_user(user)
        self.assertIsNotNone(user_id)
        user = {
            "user_id": "12345678",
            "name": "edit",
            "email": "edit",
            "image_url": "edit"
        }
        out = self.dao.update_user(user)
        self.assertEquals(out['ok'], 1)
        updated_user = self.dao.get_user(user['user_id'])
        self.assertIsNotNone(updated_user)
        self.assertEquals(updated_user['name'], 'edit')
        self.assertEquals(updated_user['email'], 'edit')
        self.assertEquals(updated_user['image_url'], 'edit')
        try:
            self.dao.update_user({})
        except Exception, e:
            self.assertEquals(int(str(e)), 400)
        user = {
            "user_id": "123",
            "name": "John Doe",
            "email": "something@test.com",
            "image_url": "http://www.test.com/imege.jpg"
        }
        try:
            self.dao.update_user(user)
        except Exception, e:
            self.assertEquals(int(str(e)), 404)
