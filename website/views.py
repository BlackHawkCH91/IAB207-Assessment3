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

        cities = ["All"]
        for event in events:
            if event.City not in cities:
                cities.append(event.City)

        return render_template("index.html", events = events, cities = cities)
    
    events = Events.query.all()
    cities = ["All"]
    for event in events:
        if event.City not in cities:
            cities.append(event.City)

    return render_template("index.html", events = events, cities = cities) # currently incorrect

@bp.route('/UserBookingHistory')
@login_required
def userBookingHistory():
    bookings = Bookings.query.filter_by(User_id = current_user.UserId)
    return render_template("userBookingHistory.html", bookings = bookings)

@bp.route('/UserSettings')
def userSettings():
    return render_template("userSettings.html")
