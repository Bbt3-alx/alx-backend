#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
app.config["BABEL_DEFAULT_LOCAL"] = "fr"


@babel.localeselector
def get_locale():
    """Get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home():
    """Home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
