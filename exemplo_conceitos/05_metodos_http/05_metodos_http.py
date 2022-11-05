from flask import Flask, request
from json import json,dumps

app = Flask(__name__, static_folder="static")


@app.route('/', methods=["GET","POST"])
def index():
    #print(request.method, request.args)
    return json.dumps(request.args)


if __name__ == '__main__':
    app.run(debug=True)
