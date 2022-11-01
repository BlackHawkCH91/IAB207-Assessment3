from flask import Blueprint, render_template, request
from .models import Events, Bookings
from flask_login import login_required, current_user
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    #If the user search for events, return results, else, return everything else.
    search = request.args.get("search")
    if search is not None:
        eventName = "%" + request.args["search"] + "%"
        events = Events.query.filter(Events.EventName.like(eventName)).all()
        return render_template("index.html", events = events)
    
    events = Events.query.all()

    return render_template("index.html", events = events) # currently incorrect

@bp.route('/UserBookingHistory')
@login_required
def userBookingHistory():
    bookings = Bookings.query.filter_by(User_id = current_user.UserId)
    return render_template("userBookingHistory.html", bookings = bookings)

@bp.route('/UserSettings')
def userSettings():
    return render_template("userSettings.html")
