import datetime
# importing everything from peewee
from peewee import *


#using sqlit to have a databse
DATABASE = SqliteDatabase('jokes.sqlite')



# defining our joke model
class Joke(Model):
	title = CharField(),
	joke = CharField(),
	created_at = DateTimeField(default=datetime.datetime.now)

	# it gives our class instructions on how to connect to 
	# a specifc database
	class Meta:
		database = DATABASE

# this method will setup the connection to the database
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Joke], safe=True)
	
	print("Connected to DB and created tables if they weren't already there.")

	DATABASE.close()