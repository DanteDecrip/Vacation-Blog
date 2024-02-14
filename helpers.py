import json


def read_db()):
    with open('db.json') as fo:
        raw_data = fo.read()

    return json.loads(raw_data)

def write_db(data):
    with open('db.json', 'w') as fo:
        fo.write(data)
