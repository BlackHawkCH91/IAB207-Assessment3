from datetime import datetime
from xmlrpc.client import DateTime
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DateTimeField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

# Define accepted file types
ALLOWED_FILE = {'PNG','JPG','png','jpg'}


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    first_name=StringField("First Name", validators=[InputRequired()])
    last_name=StringField("Last Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

# Creates the review form
class ReviewForm(FlaskForm):
  title = StringField('Review Title', [InputRequired()]) # Must enter title
  rating = StringField('Rating out of 5', [InputRequired()]) # Must enter rating
  comment = TextAreaField('Review comment', validators=[InputRequired()]) # Must enter review comment
  submit = SubmitField('Create')

#Creates event form
class EventForm(FlaskForm):
  event_name = StringField('Event Name', validators=[InputRequired()]) # Must enter event name
  description = TextAreaField('Description', validators=[InputRequired()]) # Must enter description
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')]) # Only accepts correct file types
  location = StringField('Location', validators=[InputRequired()]) # Must enter location
  start_time = DateTimeField('Start Time', validators=[InputRequired()]) # Must enter start time
  end_time = DateTimeField('End Time', validators=[InputRequired()]) # Must enter end time
  max_tickets = StringField('Max Ticket Number', validators=[InputRequired()]) # Must enter max tickets
  submit = SubmitField("Create")