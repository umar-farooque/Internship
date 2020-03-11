from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine




app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# Now we can access the configuration variables via app.config["VAR_NAME"].

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration

# app.config.from_envvar('APP_CONFIG_FILE')

# Puts the HOME blueprint on /.

from flask_wtf.csrf import CSRFError

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


db = SQLAlchemy(app)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

from .home import home
app.register_blueprint(home)

from .admin import admin
app.register_blueprint(admin, url_prefix="/admin/")