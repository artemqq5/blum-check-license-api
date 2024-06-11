from datetime import datetime, timedelta

from data.repository.AccessRepository import AccessRepository


class AccessManager:

    def activate(self, harddrive_id, uuid_key):
        access = AccessRepository().access(uuid_key)

        if not access:
            return [False, "Доступа не існує"]

        if access['harddrive_id'] is None:
            return self.__activate_access(access, harddrive_id)

        if access['harddrive_id'] != harddrive_id:
            return [False, "Доступ прив'язано до іншого пристрою"]

        if datetime.now() > access['end_time']:
            return [False, "Доступ просрочено"]

        if access['harddrive_id'] == harddrive_id:
            return [True, "Доступ дозволено"]

    @staticmethod
    def __activate_access(access, harddrive_id):
        start_time = datetime.now()
        end_time = start_time + timedelta(days=access['days'])

        if not AccessRepository().activate(start_time, end_time, harddrive_id, access['uuid_key']):
            return [False, "Невдалося активувати доступ"]

        return [True, "Доступ активовано"]
