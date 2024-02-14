from helpers import read_db, write_db


class Users:
    def __init__(self):
        self.db = read_db()

    def __commit(self):
        write_db(self.db)

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

        self.db['users'].append(new_user)
        self.__commit()

        return new_user
        
    def delete(self, username):
        popped_user = None
        for idx, user in enumerate(self.db['users']):
            if user['username'] == username:
                popped_user = self.db['users'].pop(idx)

        self.__commit()
        return popped_user
