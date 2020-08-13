from july_blog import app, db, Message, mail
from flask import render_template, request , redirect, url_for

#Import the form
from july_blog.forms import UserInfoForm
from july_blog.forms import BlogPostForm
from july_blog.forms import LoginForm

#Import from Models
from july_blog.models import User, Post, check_password_hash


#Import for Flask-logins - loginrequired, current usaer and logout _user
from flask_login import login_required, login_user, current_user, logout_user

#Home page route
@app.route('/')  # decorator
def home():
    #to see all postst on home page
    posts= Post.query.all()
    return render_template("home.html", posts=posts)

#Register route
@app.route('/register', methods= ['GET','POST'])  # decorator
def register():
    form = UserInfoForm()
    #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
    # if the request == post then the user in fo entered is SENT
    if request.method == 'POST' and form.validate():
        #Get Information - these are the values for the insert stmt
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username,password,email)  # this will print out in terminal
        #Creat and instance of User look at the __init__ in models
        user = User(username, email, password)
        #Open and insert into db - connecting to db like an insert statement
        db.session.add(user)
        # lik git add and then commit Save info to db
        db.session.commit()

        #Flask email sender
        msg = Message(f'Thanks for signing up, {username}', recipients= [email])
        msg.body= ('Congrats on signing up!')
        msg.html = ('<h1> Welcome to the July Blog!</h1>' '<p> This will be fun</p>')

        mail.send(msg)
    return render_template("register.html", form=form)

#Create a blog route
@app.route('/createposts', methods=['GET','POST'])
@login_required    # chaecking in that the user if not loggged in
def createposts():
    form = BlogPostForm()
    if request.method == 'POST' and form.validate():
        title= form.title.data
        content = form.content.data 
        print("\n",title, content)   ## this will print out in terminal
        #current_user is part of the flask_login method line 14 above, the module looks after this for you
        user_id = current_user.id  # this will work because of the @login_required to , you have to be logged in
        post = Post(title, content, user_id)  #need user_id this is a FK in the talbe
        #Open and insert into db - connecting to db like an insert statement
        db.session.add(post)
        # like git add and then commit Save info to db
        db.session.commit()
        return redirect(url_for('createposts'))
    return render_template("createposts.html", form=form)


@app.route('/posts/<int:post_id>')
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)  # get_or404 throws and exception if your post_id does not exist, 404 is a clinet error
    return render_template('post_detail.html',post=post)


@app.route('/posts/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    update_form = BlogPostForm()

    if request.method == 'POST' and update_form.validate():
        title= update_form.title.data
        content = update_form.content.data
        user_id = current_user.id
        
        #Update post with more info
        post.title = title
        post.content = content
        post.user_id = user_id

        #Commit changes, we don't do add because we are just updating
        db.session.commit()
        return redirect(url_for('post_update', post_id=post.id))

    return render_template('post_update.html', update_form=update_form) 


@app.route('/posts/delete/<int:post_id>', methods=['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    #Commit changes, we don't do add because we are just updating
    db.session.commit()
    return redirect(url_for('home'))  


 
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm() # create instance of login form
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
         # runs the same hash method on the entered password and then matches
         #  the hash  - returns True or false
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login')) # this is a GET request, like a refresh
        
    return render_template ('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))