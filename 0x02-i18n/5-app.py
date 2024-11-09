#!/usr/bin/env python3
"""A user login system"""


from flask import Flask, request, g, render_template
from typing import Optional
from flask_babel import Babel, _


class Config:
    """App configuration object"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get local from url"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[dict]:
    """Get a user by its id"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> Optional[dict]:
    """Executed before all other functions"""
    g.user = get_user()


@app.route('/')
def home() -> str:
    """The home page"""
    return render_template('5-index.html', user=g.user, _=_)


if __name__ == "__main__":
    app.run(debug=True)

