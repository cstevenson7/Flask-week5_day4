from flask import Flask
from config import Config

# import for Flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# import for flask mail
from flask_mail import Mail, Message

#import for flask login
from flask_login import LoginManager
app= Flask(__name__)

app.config.from_object(Config)  # pulling in our config calss

db= SQLAlchemy(app)
migrate = Migrate(app,db)

mail = Mail(app)

#login Confin
login = LoginManager(app)
login.login_view = 'login'  # specify what page to load for NON- authentcated Users

from july_blog import routes  
from july_blog import models

