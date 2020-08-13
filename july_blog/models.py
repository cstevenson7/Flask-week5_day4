from july_blog import app,db, login 
from werkzeug.security import generate_password_hash, check_password_hash 

from datetime import datetime

#Imports for User Mixin
#To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations for all of #these properties and methods.
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#inheriting from the __init__ db
class User(db.Model, UserMixin):
    # setting id to primary key
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    #Helping to set up a firgieng key a many to one relationship
    post = db.relationship('Post', backref='author', lazy=True ) 

    def __init__(self,username,email,password):
        self.username= username
        self.email = email
        self.password = self.set_password(password)
    
    # don't want passwords in our database
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
     

    def __repr__(self):
        return f'{self.username} has been created with {self.email}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    #ALWAYS SAVE DATETIME AS UTC TIME  saves issues down the road.
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    #this will print in terminal 99% of the time
    def __repr__(self):
        return f'The title of the post is {self.title} \n and the content is {self.content}'


        