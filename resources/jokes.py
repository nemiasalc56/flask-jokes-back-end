import models

from flask import Blueprint



# the first arg is the blueprint's name
# and the second arg is its import_name
jokes = Blueprint('jokes', 'jokes')


# this is goind to be the index route
@jokes.route('/', methods=['GET'])
def jokes_index():

	return "jokes resource is working!"


# create route
@jokes.route('/', methods=['POST'])
def create_joke():
	return "you hit the craete route"