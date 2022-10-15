from . import db
from datetime import datetime

#Classes have been created per Christians database model.
#corrections for a later date, password hashing, confirm rating implimentation
class Users(db.Model):
    __tablename__='Users'
    UserId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100), index=True, nullable=False)
    LastName = db.Column(db.String(100), index=True, nullable=False)
    Email = db.Column(db.String(100), index=True, nullable=False)
	#encrypted password is stored
	#at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.Reviews and Reviews.created_by
    Reviews = db.relationship('Reviews', backref='UserId')
    # relation to call user.Bookings
    Bookings = db.relationship('Bookings', backref='UserId')

class Events(db.Model):
    __tablename__ = 'Events'
    EventId = db.Column(db.Integer, primary_key=True)
    EventName = db.Column(db.String(80))
    EventStatus = db.Column(db.String(80)) #set values / constructor restrictions 
    Location = db.Column(db.String(80))
    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    Image = db.Column(db.String(400))
    MaxTickets = db.Column(db.Interger)
    
	#relations
    Reviews = db.relationship('Reviews', backref='EventId')
    Bookings = db.relationship('Bookings', backref='EventId')
    #Foriegn Key
    Catergory_id = db.Column(db.Integer, db.ForeignKey('Catergory.id'))
    
    def __repr__(self): #print
        return "<Event: {}>".format(self.name)
class Catergory(db.Model):
    __tablename__ = 'Categories'
    CatergoryId = db.Column(db.Integer, primary_key=True)
    CatergoryName = db.Column(db.String(100))

    def __repr__(self):
        return "<Catergory: {}>".format(self.text)
class Reviews(db.Model):
    __tablename__ = 'Reviews'
    ReviewId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Content = db.Column(db.String(400))
    CreatedAt = db.Column(db.DateTime, default=datetime.now())
    # to be corrected, confirm with Christian regarding implimentation 
    Rating = db.Column(db.String(400))
    
    #foreign keys
    User_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    Event_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    
    def __repr__(self):
        return "<Review: {}>".format(self.text)
    
class Bookings(db.Model):
    __tablename__ = 'Bookings'
    BookingId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Content = db.Column(db.String(400))
    BookedOn = db.Column(db.DateTime, default=datetime.now())
    TicketNum = db.Column(db.Interger)
    #foreign keys
    User_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    Event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))
    
    def __repr__(self):
        return "<Booking: {}>".format(self.text)