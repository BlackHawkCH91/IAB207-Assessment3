from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/UserBookingHistory')
def userBookingHistory():
    return render_template("userBookingHistory.html")

@bp.route('/EventCreation')
def eventCreation():
    return render_template("eventCreation.html")

@bp.route('/Event')
def event():
    return render_template("event.html")