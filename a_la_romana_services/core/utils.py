from pymongo import MongoClient
from a_la_romana_services.config import settings as s


db_name = "a_la_romana_test_db"
users = "test_users"
activities = "test_activities"
events = "test_events"


def is_valid_user(user):
    keys = ['user_id', 'name', 'email', 'image_url']
    return all(key in user for key in keys)


def clean_test_db():
    client = MongoClient()
    db = client[s.test_db_name]
    db.drop_collection(s.test_users)
    db.drop_collection(s.activities)
    db.drop_collection(s.test_events)


class InvalidUsage(Exception):

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
