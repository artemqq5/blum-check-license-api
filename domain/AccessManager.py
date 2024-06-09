from datetime import datetime, timedelta

from data.repository.AccessRepository import AccessRepository


class AccessManager:

    def activate(self, access, harddrive_id):
        if not access:
            return False

        if not self.__is_free(access):
            return False

        start_time = datetime.now()
        end_time = start_time + timedelta(days=access['days'])

        if not AccessRepository().activate(start_time, end_time, harddrive_id, uuid_key):
            return False

        return True

    def check(self, access, harddrive_id):
        if not access:
            return False

        if self.__is_free(access):
            return False

        subscribe_active = datetime.now() < access['end_time']
        if access['harddrive_id'] != harddrive_id or not subscribe_active:
            return False

        return True

    @staticmethod
    def __is_free(access):
        if not access['harddrive_id'] and not access['start_time'] and not access['end_time']:
            return True

        return False



