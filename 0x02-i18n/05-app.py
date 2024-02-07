#!/usr/bin/env python3
''' 0-app.py '''

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

app: Flask = Flask(__name__)
babel: Babel = Babel(app)
# app = Flask(__name__)
# babel = Babel(app)


class Config:
    ''' language configuration '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    ''' retrieves a user '''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    ''' before request '''
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    ''' determine the best match with our supported languages '''
    locale_param = request.args.get('locale', '')
    if locale_param in app.config["LANGUAGES"]:
        return locale_param

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    ''' index page '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
