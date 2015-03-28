import redis


class RegUser:
    def __init__(self):
        self.db = redis.Redis(host='localhost', port=6379, db=0)

    def __create_keys(self, email, user_name, password):
        self.db.set(user_name, email)
        self.db.set(email, password)
        self.db.bgsave()


    def already_exist(self, email, user_name, password):
        if (self.db.exists(email) is True) \
                or (self.db.exists(user_name) is True):
            return True

        self.__create_keys(email, user_name, password)
        return False
