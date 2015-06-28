import json
from flask import Blueprint
from flask import request
from flask import Response
from bson import json_util
from flask.ext.cors import cross_origin
from a_la_romana_services.core.dao import DAO
from a_la_romana_services.config.settings import config


dao_rest = Blueprint('dao_rest', __name__)


@dao_rest.route('/users/')
@cross_origin(origins='*', headers=['Content-Type'], methods=['GET'])
def get_users():
    dao = DAO(config)
    users = json.dumps([_user for _user in dao.get_user(None)],
                       sort_keys=True,
                       indent=4,
                       default=json_util.default)
    return Response(users, content_type='application/json; charset=utf-8')


@dao_rest.route('/users/')
@cross_origin(origins='*', headers=['Content-Type'], methods=['POST', 'OPTIONS'])
def create_user():
    print request
    print request.remote_addr
    print request.get_json()
    user = json.loads(request.get_json())
    print user
    dao = DAO(config)
    users = json.dumps([_user for _user in dao.create_user(user)],
                       sort_keys=True,
                       indent=4,
                       default=json_util.default)
    return Response(users, content_type='application/json; charset=utf-8')
