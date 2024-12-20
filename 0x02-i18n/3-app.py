#!/usr/bin/env python3
"""Basic Babel setup"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """App configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get locale to determine the best match with supported languages
    """
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """
    Home page - just display Hello world!
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
