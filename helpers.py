import json


def __read_json():
    with open('db.json') as fo:
        raw_data = fo.read()

    return json.loads(raw_data)

def all_users():
    return __read_json()['users']

def get_user_by_name(username):
    users = all_users()

    for user in users:
        if user['username'] == username:
            return user

    return None
