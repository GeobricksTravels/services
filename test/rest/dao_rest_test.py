import json
import unittest
from flask import Flask
from pymongo import MongoClient
from a_la_romana_services.rest.dao_rest import dao_rest
from a_la_romana_services.core.utils import clean_test_db
from a_la_romana_services.config import settings as s


class DaoRestTest(unittest.TestCase):

    db = None
    client = None
    users = s.test_users
    events = s.test_events
    db_name = s.test_db_name
    activities = s.test_activities

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(dao_rest, url_prefix='/rest')
        self.tester = self.app.test_client(self)
        clean_test_db()

    def tearDown(self):
        clean_test_db()

    def clean_db(self):
        self.client = MongoClient() if self.client is None else self.client
        self.db = self.client[self.db_name] if self.db is None else self.db
        self.db.drop_collection(self.users)
        self.db.drop_collection(self.activities)
        self.db.drop_collection(self.events)

    def test_get_users(self):
        response = self.tester.get('/rest/users/test/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        out = json.loads(response.data)
        self.assertEquals(len(out), 0)

    def test_create_user(self):
        user = {
            "user_id": "12345678",
            "name": "John Doe",
            "email": "something@test.com",
            "image_url": "http://www.test.com/image.jpg"
        }
        response = self.tester.post('/rest/users/test/',
                                    data=json.dumps(user),
                                    content_type='application/json')
        self.assertEquals(response.status_code, 200)
        out = json.loads(response.data)
        self.assertIsNotNone(out)
        self.assertIsNotNone(out["$oid"])
