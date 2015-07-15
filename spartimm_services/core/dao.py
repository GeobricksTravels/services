from pymongo import MongoClient
from spartimm_services.core import utils
from spartimm_services.config import settings
from bson.objectid import ObjectId


class DAO:

    # Internal parameters.
    db_name = None
    users = None
    activities = None
    events = None
    client = None
    db = None

    def __init__(self, config):
        try:
            self.db_name = settings.db_name if config['db_name'] is None else config['db_name']
        except KeyError:
            self.db_name = settings.db_name
        try:
            self.users = settings.users if config['users'] is None else config['users']
        except KeyError:
            self.users = settings.users
        try:
            self.activities = settings.activities if config['activities'] is None else config['activities']
        except KeyError:
            self.activities = settings.activities
        try:
            self.events = settings.events if config['events'] is None else config['events']
        except KeyError:
            self.events = settings.events
        self.client = MongoClient()
        self.db = self.client[self.db_name]

    def create_user(self, user):
        if utils.is_valid_user(user):
            collection = self.db[self.users]
            existing_user = self.get_user(user['user_id'])
            if existing_user is None:
                return collection.insert(user)
            else:
                return self.get_user(user['user_id'])
        else:
            raise Exception(400)

    def get_user(self, user_id):
        collection = self.db[self.users]
        if user_id is not None:
            return collection.find_one({'user_id': user_id})
        else:
            return collection.find()

    def delete_user(self, user_id):
        existing_user = self.get_user(user_id)
        if existing_user is not None:
            collection = self.db[self.users]
            return collection.remove({'user_id': existing_user['user_id']})
        else:
            raise Exception(404)

    def update_user(self, user):
        if utils.is_valid_user(user):
            collection = self.db[self.users]
            existing_user = self.get_user(user['user_id'])
            if existing_user is not None:
                return collection.update({'user_id': existing_user['user_id']}, user, upsert=False)
            else:
                raise Exception(404)
        else:
            raise Exception(400)

    def get_event(self, event_id):
        collection = self.db[self.events]
        if event_id is not None:
            return collection.find_one({'_id': ObjectId(event_id)})
        else:
            return collection.find()

    def create_event(self, event):
        if utils.is_valid_event(event):
            collection = self.db[self.events]
            try:
                existing_event = self.get_event(event['_id'])
            except KeyError:
                return collection.insert(event)
            if 'pymongo.cursor.Cursor' in str(type(existing_event)):
                return collection.insert(event)
        else:
            raise Exception(400)

    def get_activity(self, event_id):
        collection = self.db[self.activities]
        if event_id is not None:
            return collection.find({'event_id': event_id})
        else:
            return collection.find()
