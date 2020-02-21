import os
import datetime
# importing everything from peewee
from peewee import *

# import the module that we will use to setup our login
from flask_login import UserMixin
from playhouse.db_url import connect


if 'ON_HEROKU' in os.environ: # later we will manually add this env var 
                              # in heroku so we can write this code
  DATABASE = connect(os.environ.get('DATABASE_URL')) # heroku will add this 
                                                     # env var for you 
                                                     # when you provision the
                                                     # Heroku Postgres Add-on
else:
	#using sqlit to have a databse
	DATABASE = SqliteDatabase('jokes.sqlite')


# User class must have some methods and parameters that model from peewee doesn't have
class User(UserMixin, Model):
	first_name = CharField()
	last_name = CharField()
	username = CharField(unique=True)
	password = CharField()
	email = CharField(unique=True)

	class Meta:
		database = DATABASE



# defining our joke model
class Joke(Model):
	title = CharField()
	joke = CharField()

	# set up one to many relationship between jokes and user with the foreign key
	owner = ForeignKeyField(User, backref='jokes')
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