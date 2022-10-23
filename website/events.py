from unicodedata import category
from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from .models import *
from .forms import EventForm, ReviewForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from datetime import datetime

bp = Blueprint('event',__name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = Events.query.filter_by(EventId=id).first()
    status = EventStatus.query.filter_by(EventStatusId=event.Status_id).first()
    catergory = Catergory.query.filter_by(CatergoryId=event.Catergory_id).first()
    cform = ReviewForm()
    return render_template('/event.html', event=event,status = status, catergory = catergory, form=cform)

@bp.route('/eventcreation', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():
    #checks and returns image
    db_file_path=check_upload_file(form)
    event=Events(EventName=form.event_name.data,description=form.description.data, 
    Image=db_file_path,Location=form.location.data, StartDate=form.start_time.data,
     EndDate=form.end_time.data, MaxTickets=form.max_tickets.data,
     Catergory_id=form.Catergory_id.data, Status_id=form.Status_id.data,
     UserId=current_user.UserId)
    db.session.add(event)
    db.session.commit()
    print('Successfully created new sports event', 'success')
    #redirect
    return redirect(url_for('event.create'))
  return render_template('eventCreation.html', form=form, current_user = current_user)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)
  upload_path=os.path.join(BASE_PATH,'static/img',secure_filename(filename))
  db_upload_path='/static/img/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<EventId>/comment', methods = ['GET', 'POST'])  
@login_required
def review(EventId):  
    form = ReviewForm()  
    event_obj = Events.query.filter_by(EventId=EventId).first() 
    print(current_user); 
    if form.validate_on_submit():  
      #read the comment from the form
      review = Reviews(title=form.title.data,
                       rating=form.rating.data,
                       comment=form.comment.data,
                       submit=form.submit.data,
                       user=current_user ) 
      db.session.add(review) 
      db.session.commit() 
      print('Your review has been added', 'success') 
    return redirect(url_for('events.event', EventId=EventId))

@bp.route('/update', methods = ['GET', 'POST'])  
@login_required
def update():  
    events = Events.query.filter_by(UserId = current_user.UserId)
    return render_template("myEvents.html", events = events)
 
@bp.route('/update/<EventId>', methods = ['GET', 'POST'])  
#update this to if userid == event.userid then continue, any one logged in can access atm
#if they type in the url
@login_required
def updateEvent(EventId):  
    form = EventForm()
    #event = Events.query.get(EventId)
    event = Events.query.filter_by(EventId=EventId).first()
    #prefill form with current values
    # this if is required otherwise the variables dont update or i could split the methods like
    # sheru does
    if request.method == "GET":
      form.event_name.data = event.EventName
      form.description.data = event.description
      form.location.data = event.Location
      form.Catergory_id.data = event.Catergory_id
      form.start_time.data = event.StartDate
      form.end_time.data = event.EndDate
      form.Status_id.data = event.Status_id
      form.max_tickets.data = event.MaxTickets
    #if valid submit form and update db
    if request.method == "POST" and form.validate_on_submit:
      event.EventName = form.event_name.data
      event.Location = form.location.data
      event.description = form.description.data
      event.StartDate = form.start_time.data
      event.EndDate = form.end_time.data
      event.MaxTickets = form.max_tickets.data
      event.Status_id = form.Status_id.data
      event.Catergory_id = form.Catergory_id.data
      #try commit if db error returns to values before changed
      try:
        db.session.commit()
        return render_template('UpdateEvent.html',EventId = EventId, event = event, form = form)
      except:
        return render_template('UpdateEvent.html',EventId = EventId, event = event, form = form)
    
    return render_template('UpdateEvent.html',EventId = EventId, event = event, form = form)