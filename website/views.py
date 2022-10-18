from re import search
from urllib import request
from flask import Blueprint, render_template, request
from .models import Events, Catergory 
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    #If the user search for events, return results, else, return everything else.
    if request.args["search"]:
        eventName = "%" + request.args["search"] + "%"
        events = Events.query.filter(Events.EventName.like(eventName)).all()
        return render_template("index.html", events = events)

    events = Events.query.all()
    return render_template("index.html", events = events)

@bp.route('/UserBookingHistory')
def userBookingHistory():
    return render_template("userBookingHistory.html")

@bp.route('/EventCreation')
def eventCreation():
    return render_template("eventCreation.html")

@bp.route('/Event')
def event():
    return render_template("event.html")

@bp.route('/UpdateEvent')
def updateEvent():
    return render_template("updateEvent.html")

@bp.route('/UserSettings')
def userSettings():
    return render_template("userSettings.html")
