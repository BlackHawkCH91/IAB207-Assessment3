#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

#initialize the login manager
login_manager = LoginManager()

app=Flask(__name__)  # this is the name of the module/package that is calling this app

#create a function that creates a web application
# a web server will run this web application
def create_app():
  
    app.debug=True
    app.secret_key='utroutoru'
    #set the app configuration data 
    #Renamed DB for ease of use
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Events.sqlite'
    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)
    
    
    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    # Intitialise Login Manager
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    # Create loader function that takes a user ID and returns a User
    from .models import Users # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # Handle 404 error
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
        return render_template("404.html")


    #importing views module here to avoid circular references
    # a commonly used practice.
    from . import views
    app.register_blueprint(views.bp)

    from . import events
    app.register_blueprint(events.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app



