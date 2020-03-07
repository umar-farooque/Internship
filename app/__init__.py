from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# Now we can access the configuration variables via app.config["VAR_NAME"].


# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration

# app.config.from_envvar('APP_CONFIG_FILE')

# Puts the HOME blueprint on /.




db = SQLAlchemy(app)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

from .home import home
app.register_blueprint(home)

from .admin import admin
app.register_blueprint(admin, url_prefix="/admin/")