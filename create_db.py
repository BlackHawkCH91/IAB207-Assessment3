#running this file will recreate db
from website import db, create_app
app=create_app()
ctx=app.app_context()
ctx.push()
db.create_all()
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
