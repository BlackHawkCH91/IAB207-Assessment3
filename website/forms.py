from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import validators
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, SelectField, IntegerField, DecimalField, DateTimeLocalField, RadioField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError, NumberRange
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
    number = StringField("Contact Number", validators=[InputRequired()])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

star = Markup('<span class="fa fa-star rating"></span>')
# Creates the review form
class ReviewForm(FlaskForm):
  title = StringField('Review Title', [InputRequired()]) # Must enter title
  rating = RadioField(star, validators=[InputRequired()], choices=[(1,1), (2,2), (3,3), (4,4), (5,5)]) # Must enter rating
  comment = TextAreaField('Review comment', [InputRequired()]) # Must enter review comment
  submit = SubmitField('Post')

#Creates event form
class EventForm(FlaskForm):
  event_name = StringField('Event Name', validators=[InputRequired()]) # Must enter event name
  description = TextAreaField('Description', validators=[InputRequired()]) # Must enter description
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')]) # Only accepts correct file types
  location = StringField('Location', validators=[InputRequired()]) # Must enter location
  city = StringField('City', validators=[InputRequired()]) # Must enter location
  Catergory_id = SelectField(u'Select Sport', choices=[(1, 'Basketball'), (2, 'Cricket'), (3, 'Gymnastics'), (4, 'Netball'),
  (5, 'Football'), (6, 'Rugby'), (7, 'Swimming'), (8, 'Tennis')], validators=[InputRequired()])
  start_time = DateTimeLocalField('Start Time', validators=[InputRequired()], format="%Y-%m-%dT%H:%M", description="YYYY-MM-DD HH:MM:SS") # Must enter start time
  end_time = DateTimeLocalField('End Time', validators=[InputRequired()], format="%Y-%m-%dT%H:%M", description="YYYY-MM-DD HH:MM:SS") # Must enter end time
  max_tickets = IntegerField('Max Ticket Number', validators=[InputRequired(), NumberRange(min=0, max=5000)]) # Must enter max tickets
  ticket_price = StringField('Ticket Price', [InputRequired(), validators.Regexp('^[^\-]\d*\.?\d*$')]) # Must enter ticket price
  #ticket_price = DecimalField('Ticket Price', validators=[InputRequired(), NumberRange(min=0, max=1000)]) # Must enter price
  Status_id = SelectField(u'Select status', choices=[(1, 'Upcoming'), (2, 'Unpublished'), (3, 'Sold-out'), (4, 'Cancelled')], validators=[InputRequired()])
  submit = SubmitField("Submit")
  
class EventUpdate(FlaskForm):
  description = TextAreaField('Description', validators=[InputRequired()]) # Must enter description
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')]) # Only accepts correct file types
  start_time = DateTimeLocalField('Start Time', validators=[InputRequired()], format="%Y-%m-%dT%H:%M", description="YYYY-MM-DD HH:MM:SS") # Must enter start time
  end_time = DateTimeLocalField('End Time', validators=[InputRequired()], format="%Y-%m-%dT%H:%M", description="YYYY-MM-DD HH:MM:SS") # Must enter end time
  max_tickets = IntegerField('Max Ticket Number', validators=[InputRequired(), NumberRange(min=0, max=5000)]) # Must enter max tickets
  ticket_price = DecimalField('Ticket Price', validators=[InputRequired(), NumberRange(min=0, max=1000)]) # Must enter max tickets
  Status_id = SelectField(u'Select status', choices=[(1, 'Upcoming'), (2, 'Unpublished'), (3, 'Sold-out'), (4, 'Cancelled')], validators=[InputRequired()])
  submit = SubmitField("Submit")

# Creates Booking Form
class BookingForm(FlaskForm):
  ticket_num = IntegerField('Number of Tickets', validators=[InputRequired(), NumberRange(min=0)]) #Must enter number of tickets
  submit = SubmitField("Submit")