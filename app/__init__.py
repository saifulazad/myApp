


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
 
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from flask_wtf.csrf import CsrfProtect

login_manager.init_app(app)
csrf = CsrfProtect()


csrf.init_app(app)

from app import views, models
