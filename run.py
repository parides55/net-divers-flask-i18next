import os
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'   # default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'el']  # add your languages


# Define locale selector function
def get_locale():
    return request.args.get('lang') or request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Pass it into Babel
babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/secondary')
def secondary():
    return render_template("secondary.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )