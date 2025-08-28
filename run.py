import os
import json
from flask import Flask, render_template, request, session, redirect, url_for
from flask_babel import Babel, _
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.config['BABEL_DEFAULT_LOCALE'] = 'en'   # default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'el']  # add your languages


# Locale selector function
def get_locale():
    # First check session
    if 'lang' in session:
        return session['lang']
    # Fallback to browser preference
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


# Pass it into Babel
babel = Babel(app, locale_selector=get_locale)


# Route to change language
@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    if lang_code in app.config['BABEL_SUPPORTED_LOCALES']:
        session['lang'] = lang_code
    return redirect(request.referrer or url_for('index'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/secondary')
def secondary():
    return render_template("secondary.html")


@app.route('/explore_cy')
def explore_cy():
    return render_template("explore_cy.html")
    

@app.route('/diving_sites')
def diving_sites():
    return render_template("diving_sites.html")


@app.route('/courses_and_services')
def courses_and_services():
    data = []
    with open('data/courses_services.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("courses_and_services.html", courses=data)


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )