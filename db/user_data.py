"""
 key-value pair DB
"""
import json


class DB:
    data = dict()


def create_user(user_id, user=None):
    if db.get(user_id, None) or check_duplicate(user):
        return False
    db.update({user_id: user})
    return True


def update_user(user_id, user=None):
    if db.get(user_id, None):
        db.update({user_id: user})
        return True
    return False


def delete_user(user_id):
    return db.pop(user_id, None)


def get_user(user_id):
    return db.get(user_id, None)


def check_duplicate(user):
    for _,value in db.items():
        if user.get("username", None) == value.get("username", None):
            return True
    return False


db = DB().data
