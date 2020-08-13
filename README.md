
README
WeekDay4 FLask database/email/login/


# to activate your VE
D:\Coding_Temple\week5\day1\Project>blog_july_env\scripts\activate.bat


# need to do this before you run the first flask run of the day
set FLASK_APP=app.py

set FLASK_ENV=development



pip install Flask-WTF

pip install email-validator

pip install Flask-SQLAlchemy Flask-Migrate

flask db init

flask db migrate -m "Create User and Post"

flask db upgrade


SyntaxError: invalid syntax

(blog_july_env) D:\Coding_Temple\week5\day3>flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

after running flask shell

>>> from july_blog.models import User, Post
>>> from july_blog import app, db
>>> user_test = User("test123", "test123@gmail.com", "est123")  
>>> db.session.add(user_test)
>>> db.session.commit() 
>>> user_test.id
2
>>>

>>> User.query.all()
[wilma has been created with wilma@gmail.com, test123 has been created with test123@gmail.com]
# filtering  by object
>>> User.query.filter_by(id=1)
<flask_sqlalchemy.BaseQuery object at 0x00000198DB6587C8>
>>> User.query.filter_by(id=1).first()
wilma has been created with wilma@gmail.com
>>>

>>> User.query.filter(User.email.endswith('@gmail.com')).first()
wilma has been created with wilma@gmail.com
>>> 

# get users by Primary Key

>>> User.query.get(2) 
test123 has been created with test123@gmail.com
>>>

# order by primary key
>>> User.query.order_by(User.id).all() 
[wilma has been created with wilma@gmail.com, test123 has been created with test123@gmail.com]


# order by desc
>>> User.query.order_by(User.email.desc()).all()
[wilma has been created with wilma@gmail.com, test123 has been created with test123@gmail.com]
>>>
>>> 

# if you change anything in your  .py code you have to re-satart the shell


blog_july_env) D:\Coding_Temple\week5\day3>flask shell
Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] on win32
App: july_blog [production]
Instance: D:\Coding_Temple\week5\day3\instance
>>> from july_blog.models import User, Post
>>> from july_blog import app, db
>>> user_test=User.query.get(2)
>>> user_test
test123 has been created with test123@gmail.com
>>> post1=Post("this is title", "fun", user_test.id)
>>> post1
The title of the post is this is title
 and the content is fun
>>> db.session.add
<bound method instrument.<locals>.do of <sqlalchemy.orm.scoping.scoped_session object at 0x0000028C22599A88>>
>>> db.session.add(post1)
>>> db.session.commit
<bound method instrument.<locals>.do of <sqlalchemy.orm.scoping.scoped_session object at 0x0000028C22599A88>>
>>> db.session.commit()
>>> post2 = Post("aamother title", "still fun", user_test.id)
>>> db.session.add(post2)
>>> db.session.commit()
>>> Post.query.all()
[The title of the post is this is title
 and the content is fun, The title of the post is aamother title
 and the content is still fun]

 post = Post.query.filter_by(id=1).first()
 # can do theis because of the relationship we created in models.py
 test_author = post.author
test_author.id
 test_author.post


 pip install flask-login
 
  Betty 12345 cindy.stevenson1+1@gmail.com

 # *********** Day 4
#try below if things are weird
 conda deactivate

# to remove a user from the database 
look at Week5  day4 screen shots

 To remove a file from github
git rm --cached app.db - this semmed to remove the app.db from the 

# FOR Herocu

create Procfile file
pip install gunicorn pillow psycopg2

#  this create a text file of all the versions of you modules
pip freeze > requirements.txt 


# handy command - this was the mac command
"/usr/local/bin:$PATH"
