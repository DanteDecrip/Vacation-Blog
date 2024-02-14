from helpers import read_db, write_db


class Users:
    def __init__(self):
        pass

    def all(self):
        db = read_db()

        return db['users']

    def get(self, username)
        all_users = self.all()

        for i in range(len(all_users)):
            if all_users[i]['username'] == username:
                return all_users[i]

        return None

    def create(self, new_username, new_password):
        new_user = {
            'username': new_username,
            'password': new_password,
        }

        db = read_db()
        db['users'].append(new_user)
        write_db(db)
