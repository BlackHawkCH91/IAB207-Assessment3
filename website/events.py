from flask import Blueprint, render_template, session, request, redirect, url_for
from .models import *
from .forms import EventForm, ReviewForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

bp = Blueprint('event',__name__, url_prefix='/events')

@bp.route('/<EventId>')
def show(EventId):
    event = Events.query.filter_by(EventId=EventId).first()
    cform = ReviewForm()
    return render_template('/event.html', event=event, form=cform)

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
     EndDate=form.end_time.data, MaxTickets=form.max_tickets.data, Catergory_id=form.Catergory_id.data, Status_id=form.Status_id.data )
    db.session.add(event)
    db.session.commit()
    print('Successfully created new sports event', 'success')
    #redirect
    return redirect(url_for('event.create'))
  return render_template('eventCreation.html', form=form)

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