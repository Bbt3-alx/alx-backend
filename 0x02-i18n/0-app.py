#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template, redirect, url_for
from flask_babel import Babel


def get_local():
    return ""


app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
app.config["BABEL_DEFAULT_LOCAL"] = "fr"


@app.route("/")
def home():
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
