#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """App configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """Get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# app.config.from_pyfile('mysettings.cfg')
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    """Home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
