#!/usr/bin/env python3
''' 0-app.py '''

from flask import Flask, render_template, request
from flask_babel import Babel

# app: Flask = Flask(__name__)
# babel: Babel = Babel(app)
# app = Flask(__name__)
# babel = Babel(app)


class Config:
    ''' language configuration '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
# app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    ''' determine the best match with our supported languages '''
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    ''' index page '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
