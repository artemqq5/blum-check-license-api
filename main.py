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
        return "Error: auth wrong params", 401

    if not uuid_key or not harddrive_id:
        return "Error: miss some params", 402

    access = AccessRepository().access(uuid_key)

    if not AccessManager().check(access, harddrive_id):
        return "Error: permission denied", 404

    return access, 200


@app.route("/activate", methods=['GET'])
def license_activation():
    key = request.args.get("token", None)
    uuid_key = request.args.get("uuid_key", None)
    harddrive_id = request.args.get("harddrive_id", None)

    if key != AUTHORIZATION_TOKEN:
        return "Error: auth wrong params", 401

    if not uuid_key or not harddrive_id:
        return "Error: miss some params", 402

    access = AccessRepository().access(uuid_key)

    if not AccessManager().activate(access, harddrive_id):
        return "Error: permission denied", 404

    return access, 200


if __name__ == '__main__':
    app.run()
    # http_server = WSGIServer(("0.0.0.0", 5020), app)
    # http_server.serve_forever()
