#!/usr/bin/env python3
''' 5-app.py '''

from flask import Flask, render_template, g, request
from flask_babel import Babel, _

app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    ''' language configuration '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users: dict = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict:
    ''' getting user '''
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    ''' before request '''
    user_id: int = int(request.args.get('login_as', 0))
    g.user: dict = get_user(user_id) if user_id else None


@babel.localeselector
def get_locale() -> str:
    ''' get locale '''
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    ''' index page '''
    if g.user:
        welcome_message: str = (
                _(
                    "You are logged in as %(username)s."
                ) % {'username': g.user['name']}
        )
    else:
        welcome_message: str = _("You are not logged in.")
    return render_template('6-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
