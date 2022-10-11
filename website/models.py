from . import db
from datetime import datetime
from flask_login import UserMixin

#Classes have been created per Christians database model.
#corrections for a later date, password hashing, confirm rating implimentation
class Users(db.Model, UserMixin):
    __tablename__='users'
    UserId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100), index=True, nullable=False)
    LastName = db.Column(db.String(100), index=True, nullable=False)
    Email = db.Column(db.String(100), index=True, nullable=False)
	#encrypted password is stored
	#at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation
    reviews = db.relationship('Reviews', backref='user')
    bookings = db.relationship('Bookings', backref='user')

class Events(db.Model):
    __tablename__ = 'events'
    EventId = db.Column(db.Integer, primary_key=True)
    EventName = db.Column(db.String(80))
    Location = db.Column(db.String(80))
    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    Image = db.Column(db.String(400))
    MaxTickets = db.Column(db.Interger)
    
	#relations
    reviews = db.relationship('Reviews', backref='event')
    bookings = db.relationship('Bookings', backref='event')
    #Foriegn Key
    Catergory_id = db.Column(db.Integer, db.ForeignKey('catergories.CatergoryId'))
    Status_id = db.Column(db.Integer, db.ForeignKey('eventStatus.EventStatusId'))
    
    def __repr__(self): #print
        return "<Event: {}>".format(self.name)
class EventStatus(db.Model):
    __tablename__ = 'eventStatus'
    EventStatusId = db.Column(db.Integer, primary_key=True)
    Status = db.Column(db.String(80))
    
    Event = db.relationship('Events', backref='status')
    
    def __repr__(self): #print
        return "<Event: {}>".format(self.name)
class Catergory(db.Model):
    __tablename__ = 'categories'
    CatergoryId = db.Column(db.Integer, primary_key=True)
    CatergoryName = db.Column(db.String(100))

    def __repr__(self):
        return "<Catergory: {}>".format(self.text)
class Reviews(db.Model):
    __tablename__ = 'reviews'
    ReviewId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Content = db.Column(db.String(400))
    CreatedAt = db.Column(db.DateTime, default=datetime.now())
    # to be corrected, confirm with Christian regarding implimentation 
    Rating = db.Column(db.String(400))
    
    #foreign keys
    User_id = db.Column(db.Integer, db.ForeignKey('users.UserId'))
    Event_id = db.Column(db.Integer, db.ForeignKey('events.EventId'))
    
    def __repr__(self):
        return "<Review: {}>".format(self.text)
    
class Bookings(db.Model):
    __tablename__ = 'bookings'
    BookingId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Content = db.Column(db.String(400))
    BookedOn = db.Column(db.DateTime, default=datetime.now())
    TicketNum = db.Column(db.Interger)
    #foreign keys
    User_id = db.Column(db.Integer, db.ForeignKey('users.UserId'))
    Event_id = db.Column(db.Integer, db.ForeignKey('events.EventId'))
    
    def __repr__(self):
        return "<Booking: {}>".format(self.text)