from flask import Flask
from flask import request
from config import config
from db import user_data
from common.util import create_user_reference, validate_user
from flask import jsonify
import traceback

app = Flask(__name__)


log = config.config.get_logger()

@app.route("/api/v1/users", methods=['POST'])
def create_user():
    err, code = None, 201
    try:
        log.info("New user request ".format(request.url))
        user = request.get_json()
        log.debug(user)
        user_id = create_user_reference()
        user.update({"user_id": user_id})
        if not validate_user(user.get("username", None)):
            err, code = _invalid_input()
            return _frame_response(None, err, code), code
        created = user_data.create_user(user_id, user)
        if not created:
            err, code = _already_exists()
    except Exception as ex:
        log.error(traceback.print_exc())
        err, code = _intern_error(str(ex))
    return _frame_response(_success(user_id), err, code), code


@app.route("/api/v1/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    err, code = None, 200
    try:
        log.info("Update User : {}".format(user_id))
        user = request.get_json()
        log.debug(user)
        user.update({"user_id": user_id})
        log.info(user)
        if not validate_user(user.get("username", None)):
            log.info("issue")
            err, code = _invalid_input()
            return _frame_response(None, err, code), code
        updated = user_data.update_user(user_id, user)
        if not updated:
            err, code = _not_found()
    except Exception as ex:
        log.error(traceback.print_exc())
        err, code = _intern_error(str(ex))
    return _frame_response(_success(user_id), err, code), code


@app.route("/api/v1/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    err, code = None, 200
    try:
        log.info("Delete User : {}".format(user_id))
        deleted = user_data.delete_user(user_id)
        if not deleted:
            err, code = _not_found()
    except Exception as ex:
        log.error(traceback.print_exc())
        err, code = _intern_error(str(ex))
    return _frame_response(_success(user_id), err, code), code


@app.route("/api/v1/users/<user_id>", methods=['GET'])
def get_user(user_id):
    err, code = None, 200
    try:
        log.info("Get User : {}".format(user_id))
        found = user_data.get_user(user_id)
        if not found:
            err, code = _not_found()
    except Exception as ex:
        log.error(traceback.print_exc())
        err, code = _intern_error(str(ex))
    return _frame_response(found, err, code), code


def _invalid_input():
    return "Invalid Input", 403

def _already_exists():
    return "Already Exists", 409


def _not_found():
    return "Not Found", 404


def _intern_error(ex):
    return "Internal Server Error: {}".format(ex), 500


def _success(user):
    return {"status": "success", "user_id" : user}


def _frame_response(value, err, code=500):
    if err:
        log.exception("New Beginings : API Error - {0}".format(err))
        resp = jsonify({
            "error_message": err,
            "status_code": code,
        })
    else:
        resp = jsonify(value)
    return resp


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
