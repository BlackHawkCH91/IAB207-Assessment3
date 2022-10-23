#running this file will recreate db
from unicodedata import category
from website import db, create_app
from website.models import Catergory, EventStatus
import os

os.remove("website/Events.sqlite")
app=create_app()
ctx=app.app_context()
ctx.push()
db.create_all()

categoryList = ["Basketnall", "Cricket", "Gymnastics", "Netball", "Football", "Rugby", "Swimming", "Tennis"]
EventStatuses = ["Upcoming", "Inactive", "Booked", "Cancelled"]

counter = 1

for categoryName in categoryList:
    categoryModel = Catergory(CatergoryId=counter, CatergoryName=categoryName)
    db.session.add(categoryModel)
    counter += 1

counter = 1
for StatusName in EventStatuses:
    eventStatus = EventStatus(EventStatusId=counter, Status=StatusName)
    db.session.add(eventStatus)
    counter += 1

db.session.commit()
quit()


#INSERT INTO catergories (CatergoryID, CatergiryName)
#VALUES
#	(1,"Basketball"),
#	(2, "Cricket"),
#	(3, "Gymnastics"),
#	(4, "Netball"),
#	(5, "Football"),
#	(6, "Rugby"),
#	(7, "Swimming"),
#	(8, "Tennis");

#INSERT INTO eventStatus (EventStatusID, Status)
#VALUES
#	(1,"Upcoming"),
#	(2, "Inactive"),
#	(3, "Booked"),
#	(4, "Cancelled");
