from pymongo import MongoClient
from spartimm_services.config import settings as s


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
        Exception.__init__(self)            # pragma: no cover
        self.message = message              # pragma: no cover
        if status_code is not None:         # pragma: no cover
            self.status_code = status_code  # pragma: no cover
        self.payload = payload              # pragma: no cover

    def to_dict(self):
        rv = dict(self.payload or ())       # pragma: no cover
        rv['message'] = self.message        # pragma: no cover
        return rv                           # pragma: no cover
