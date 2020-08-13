import os
basedir = os.path.abspath(os.path.dirname(__file__))  # always need these two commands

#windows = D:\Coding_Temple\week5\day1\

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess..'
    #use sql lite if you can't find the other db connection  backend connection
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #congifure app to work with sendgrid
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    
    
