from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from .models import *
from .forms import EventForm, ReviewForm, EventUpdate, BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from datetime import datetime

bp = Blueprint('event',__name__, url_prefix='/events')

@bp.route('/<id>', methods = ['GET', 'POST'])
def show(id):
    event = Events.query.filter_by(EventId=id).first()
    cform = ReviewForm()
    dform = BookingForm()
    remainder = event.MaxTickets - event.tickets_booked
    if cform.validate_on_submit():  
    #read the comment from the form
      review = Reviews(Title=cform.title.data,
                        Rating=cform.rating.data,
                        Content=cform.comment.data, 
                        User_id=current_user.UserId,
                        Event_id=id) 
      db.session.add(review) 
      db.session.commit()

    return render_template('/event.html', event=event, form=cform, dform = dform, remainder = remainder)

@bp.route('/eventcreation', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()

  if form.validate_on_submit():
    #checks and returns image
    db_file_path=check_upload_file(form)
    event=Events(EventName=form.event_name.data,description=form.description.data, 
    Image=db_file_path,Location=form.location.data, City=form.city.data, StartDate=form.start_time.data,
    EndDate=form.end_time.data, MaxTickets=form.max_tickets.data,
    Catergory_id=form.Catergory_id.data, Status_id=form.Status_id.data, tickets_booked = 0,
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

@bp.route('/update', methods = ['GET', 'POST'])  
@login_required
def update():  
    events = Events.query.filter_by(UserId = current_user.UserId)
    return render_template("myEvents.html", events = events)
 
@bp.route('/update/<EventId>', methods = ['GET', 'POST'])  
@login_required
def updateEvent(EventId):  
    form = EventUpdate()
    event = Events.query.filter_by(EventId=EventId).first()
    deleteEvent = request.form.get('delete')
    #check user is creator else deny and return to myevents page
    if current_user.UserId != event.UserId:
      flash('unauthorised access')
      return redirect(url_for('event.update'))
    #this if is required otherwise the variables dont update or i could split the methods like
    if request.method == "POST":
      #if delete pressed delete event
      if deleteEvent is not None:
        db.session.delete(event)
        db.session.commit()
        return redirect(url_for('event.update'))
      #if valid submit form and update db
      if form.validate_on_submit:
        db_file_path=check_upload_file(form)
        event.Image = db_file_path
        event.description = form.description.data
        event.StartDate = form.start_time.data
        event.EndDate = form.end_time.data
        event.MaxTickets = form.max_tickets.data
        event.Status_id = form.Status_id.data
          #try commit if db error returns to values before changed
        try:
          db.session.commit()
          return redirect(url_for('event.update'))
        except:
          flash('error resubmit')
          return render_template('/updateEvent.html',EventId = EventId, event = event, form = form)
        
    elif request.method == "GET":
       #prefill form with current values
      form.description.data = event.description
      form.image.data = event.Image
      form.start_time.data = event.StartDate
      form.end_time.data = event.EndDate
      form.Status_id.data = event.Status_id
      form.max_tickets.data = event.MaxTickets
      return render_template('/updateEvent.html',EventId = EventId, event = event, form = form)
    
def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)
  upload_path=os.path.join(BASE_PATH,'static/img',secure_filename(filename))
  db_upload_path='/static/img/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<id>/book', methods = ['GET', 'POST'])
@login_required
def book(id):  
    dform = BookingForm()  
    event = Events.query.filter_by(EventId=id).first() 
    if dform.validate_on_submit():
      booked_tickets=dform.ticket_num.data
      event.update(booked_tickets)

      if event.tickets_booked <= event.MaxTickets:
        #read the comment from the form
        booking = Bookings(Title=event.EventName,
                         Content=event.description,
                         TicketNum=dform.ticket_num.data,
                         Event_id=event.EventId,
                         User_id=current_user.UserId,
                         Status_id=event.Status_id )

        db.session.add(booking) 
        db.session.commit()
        if event.tickets_booked == event.MaxTickets:
          event.Status_id = 3
          db.session.commit()
        print('Your booking has been created', 'success')
        flash('Your booking has been created')
        return redirect(url_for('event.show', id=event.EventId))
      else:
        flash('Cannot purchase more tickets than available')
    return redirect(url_for('event.show', id=event.EventId))