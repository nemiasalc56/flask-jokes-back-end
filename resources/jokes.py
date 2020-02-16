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
	all_jokes_query = models.Joke.select()
	joke_dicts = [model_to_dict(j) for j in all_jokes_query]
	print(joke_dicts)


	return jsonify(
		data=joke_dicts,
		message=f"Successfully retrieved {len(joke_dicts)} jokes!",
		status=200
		), 200


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

	joke_dict = model_to_dict(joke)
	

	return jsonify(
		data=joke_dict,
		message= "Successfully created dog!",
		status=201
		), 201


# show route
@jokes.route('/<id>', methods=['GET'])
def get_one_joke(id):
	joke_query = models.Joke.get_by_id(id)
	print(joke_query)

	joke_dict = model_to_dict(joke_query)
	print(joke_dict)

	return jsonify(
		data=joke_dict,
		message=f"Successfully found joke with id {joke_dict['id']}",
		status=200
		), 200











