import models

from flask import Blueprint, request, jsonify

# some extra tool that we need from peewee
from playhouse.shortcuts import model_to_dict




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
	payload = request.get_json()

	print(payload['title'])
	joke = models.Joke.create(
		title=payload['title'],
		joke=payload['joke'],
		owner=payload['owner']
		)

	print(joke)
	# print("")
	# print(dir(joke))

	joke_dict = model_to_dict(joke)
	print("")
	print(joke_dict)

	return jsonify(data=joke_dict, status={'message': 'Successfully created dog!'}), 201




