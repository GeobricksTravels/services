import json
from flask import Blueprint
from flask import request
from flask import Response
from flask import jsonify
from bson import json_util
from flask.ext.cors import cross_origin
from services.core.dao import DAO
from services.config.settings import config as prod_config
from services.config.settings import test_config
from services.core.utils import InvalidUsage


dao_rest = Blueprint('dao_rest', __name__)


@dao_rest.route('/users/<config>/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_users(config):
    dao = DAO(test_config) if config == 'test' else DAO(prod_config)
    users = json.dumps([_user for _user in dao.get_user(None)],
                       sort_keys=True,
                       indent=4,
                       default=json_util.default)
    return Response(users, content_type='application/json; charset=utf-8')


@dao_rest.route('/users/<config>/', methods=['POST'])
@cross_origin(origins='*', headers=['Content-Type'])
def create_usr(config):
    dao = DAO(test_config) if config == 'test' else DAO(prod_config)
    user = json.loads(request.data)
    try:
        user_id = dao.create_user(user)
        users = json.dumps(user_id,
                           sort_keys=True,
                           indent=4,
                           default=json_util.default)
        return Response(users, content_type='application/json; charset=utf-8')
    except Exception, e:
        raise InvalidUsage('Invalid user.', status_code=int(str(e)))


@dao_rest.route('/events/<config>/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_events(config):
    dao = DAO(test_config) if config == 'test' else DAO(prod_config)
    events = json.dumps([_event for _event in dao.get_event(None)],
                        sort_keys=True,
                        indent=4,
                        default=json_util.default)
    return Response(events, content_type='application/json; charset=utf-8')


@dao_rest.route('/events/<event_id>/<config>/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_single_event(event_id, config):
    dao = DAO(test_config) if config == 'test' else DAO(prod_config)
    events = json.dumps(dao.get_event(event_id),
                        sort_keys=True,
                        indent=4,
                        default=json_util.default)
    return Response(events, content_type='application/json; charset=utf-8')


@dao_rest.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
