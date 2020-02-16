import datetime
# importing everything from peewee
from peewee import *

# import the module that we will use to setup our login
from flask_login import UserMixin


#using sqlit to have a databse
DATABASE = SqliteDatabase('jokes.sqlite')


# User class must have some methods and parameters that model from peewee doesn't have
class User(UserMixin, Model):
	first_name = CharField()
	last_name = CharField()
	username = CharField(unique=True)
	password = CharField()
	email = CharField()

	class Meta:
		database = DATABASE



# defining our joke model
class Joke(Model):
	title = CharField()
	joke = CharField()
	owner = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)

	# it gives our class instructions on how to connect to 
	# a specifc database
	class Meta:
		database = DATABASE

# this method will setup the connection to the database
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Joke], safe=True)
	
	print("Connected to DB and created tables if they weren't already there.")

	DATABASE.close()