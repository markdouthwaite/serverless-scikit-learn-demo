"""
The MIT License

Copyright (c) 2018-2020 Mark Douthwaite
"""

import flask
from main import predict_handler


app = flask.Flask("CloudFunction")


@app.route("/", methods=["POST"])
def predict():
    return predict_handler(flask.request)


app.run()
