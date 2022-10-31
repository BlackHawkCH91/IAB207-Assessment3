from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import Users
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db, login_manager


#create a blueprint
bp = Blueprint('auth', __name__)

# Login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        uname = login_form.user_name.data
        password = login_form.password.data
        u1 = Users.query.filter_by(Username=uname).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect user name'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)

        return redirect(url_for('main.index'))
    return render_template('user.html', form=login_form, heading='Login')

# Register route
@bp.route('/register', methods=['GET','POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
            #get username, password and email from the form
            uname = register.user_name.data
            fname = register.first_name.data
            lname = register.last_name.data
            pwd = register.password.data
            email=register.email_id.data
            number=register.number.data
            #check if a user exists
            u1 = Users.query.filter_by(Username=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            # don't store the password - create password hash
            pwd_hash = generate_password_hash(pwd)
            #create a new user model object
            new_user = Users(
                Username=uname, FirstName = fname, LastName = lname, 
                password_hash=pwd_hash, Email=email, ContactNumber=number)
            db.session.add(new_user)
            db.session.commit()
            #commit to the database and redirect to HTML page
            return redirect(url_for('main.index'))
    #the else is called when there is a get message
    else:
        return render_template('user.html', form=register, heading='Register')

# Logout route
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You have been logged out'

