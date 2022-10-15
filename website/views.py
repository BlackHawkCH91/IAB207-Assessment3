from flask import Blueprint, render_template
from .models import Events, Catergory 
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    events = Events.query.all()
    return render_template("index.html", events = events)

@bp.route('/UserBookingHistory')
def userBookingHistory():
    return render_template("userBookingHistory.html")

@bp.route('/Event')
def event():
    return render_template("event.html")