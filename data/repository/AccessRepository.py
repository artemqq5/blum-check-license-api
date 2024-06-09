from data.DefaultDataBase import DefaultDataBase


class AccessRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def access(self, uuid_key):
        query = "SELECT * FROM `access` WHERE `uuid_key` = %s;"
        return self._select_one(query, (uuid_key,))
    #
    # def accesses(self):
    #     query = "SELECT * FROM `access`;"
    #     return self._select(query)

    def activate(self, start_time, end_time, harddrive_id, uuid_key):
        query = "UPDATE `access` SET `start_time` = %s, `end_time` = %s, `harddrive_id` = %s WHERE `uuid_key` = %s;"
        return self._update(query, (start_time, end_time, harddrive_id, uuid_key))

