from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import Flask
UPLOAD_FOLDER = '/home/azad/myApp/app/static/img'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif', 'png'])
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
from flask_wtf.csrf import CsrfProtect

login_manager.init_app(app)
csrf = CsrfProtect()


csrf.init_app(app)

from app import views, models
