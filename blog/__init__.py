from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask('__name__', template_folder='blog/templates', static_folder='blog/static')

app.config['SECRET_KEY'] = 'secretkey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view ='admin.login'
login_manager.login_message_category ='info'

from blog.admin.routes import admin
from blog.pengunjung.routes import pengunjung

app.register_blueprint(admin)
app.register_blueprint(pengunjung)