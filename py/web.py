import os
import json
from flask import Flask
from flask import request
from clientexec import WebClientExec


app = Flask(__name__)


@app.route("/", methods=["POST"])
def web_simulation():
    client = WebClientExec()
    data = json.loads(request.get_data(as_text=True))
    client.run(data)
    return "success"


@app.route("/record/", methods=["GET"])
def controller_listen():
    case_name = request.args.get('case_name')
    os.system("./venv/bin/python py/controller.py record " + case_name + " 2>&1 &")
    return "success"


@app.route("/recover/", methods=["GET"])
def controller_recover():
    case_name = request.args.get('case_name')
    os.system("./venv/bin/python py/controller.py recover " + case_name + " 2>&1 &")
    return "success"


if __name__ == "__main__":
    app.run("127.0.0.1", "12580", debug=True)