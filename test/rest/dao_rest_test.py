import json
import unittest
from flask import Flask
from a_la_romana_services.rest.dao_rest import dao_rest


class DaoRestTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(dao_rest, url_prefix='/dao')
        self.tester = self.app.test_client(self)

    def test_list_layers(self):
        response = self.tester.get('/dao/users/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        out = json.loads(response.data)
        self.assertEquals(len(out), 0)
