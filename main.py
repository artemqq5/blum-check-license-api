from config import AUTHORIZATION_TOKEN
from flask import Flask, request
from gevent.pywsgi import WSGIServer

from data.repository.AccessRepository import AccessRepository
from domain.AccessManager import AccessManager

app = Flask(__name__)


@app.route("/check", methods=['GET'])
def check_license_handler():
    key = request.args.get("token", None)
    uuid_key = request.args.get("uuid_key", None)
    harddrive_id = request.args.get("harddrive_id", None)

    if key != AUTHORIZATION_TOKEN:
        return [False, "Error: auth wrong params"]

    if not uuid_key or not harddrive_id:
        return [False, "Error: miss some params"]

    result = AccessManager().activate(harddrive_id, uuid_key)

    if not result:
        return [False, "Error: permission denied"]
    elif not result[0]:
        return result

    access = AccessRepository().access(uuid_key)

    result.append(access)

    return result


if __name__ == '__main__':
    app.run()
    # http_server = WSGIServer(("0.0.0.0", 5000), app)
    # http_server.serve_forever()
