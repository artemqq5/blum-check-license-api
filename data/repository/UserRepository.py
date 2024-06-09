from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    # def user(self, userid):
    #     query = "SELECT * FROM `users` WHERE `userid` = %s;"
    #     return self._select_one(query, (userid,))
    #
    # def admins(self):
    #     query = "SELECT * FROM `users` WHERE `is_admin` = 1;"
    #     return self._select(query)
