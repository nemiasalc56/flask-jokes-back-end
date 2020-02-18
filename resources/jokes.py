import models
from flask_login import current_user
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

	return jsonify(
		data=joke_dicts,
		message=f"Successfully retrieved {len(joke_dicts)} jokes!",
		status=200
		), 200


# create route GET
@jokes.route('/', methods=['POST'])
def create_joke():
	payload = request.get_json()

	joke = models.Joke.create(
		title=payload['title'],
		joke=payload['joke'],
		# owner will be added later automatically with the user that is logged in
		owner=current_user.id
		)

	joke_dict = model_to_dict(joke)
	# remove password form the owner
	joke_dict['owner'].pop('password')
	
	return jsonify(
		data=joke_dict,
		message= "Successfully created dog!",
		status=201
		), 201


# show route GET
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


# update route PUT
@jokes.route('/<id>', methods=['PUT'])
def edit_joke(id):
	payload = request.get_json()
	print(payload)

	# query the joke and updated
	update_joke_query = models.Joke.update(
		title=payload['title'],
		joke=payload['joke'],
		# owner will be added later automatically with the user that is logged in
		owner=payload['owner']
		# the one that has the same id
		).where(models.Joke.id == id)
	update_joke_query.execute()
	print(update_joke_query)

	# this is the joke that was updated
	updated_joke = models.Joke.get_by_id(id)
	print(updated_joke)

	updated_joke_dict = model_to_dict(updated_joke)
	print(updated_joke_dict)

	return jsonify(
		data=updated_joke_dict,
		message=f"Successfully updated the joke with the id {updated_joke_dict['id']}",
		status=200
		), 200



# delete route DELETE
@jokes.route('/<id>', methods=['Delete'])
def delete_joke(id):
	print(id)
	# find and delete the joke with the id
	delete_query = models.Joke.delete().where(models.Joke.id == id)
	delete_query.execute()

	return jsonify(
		data={},
		message=f"Successfully deleted a joke with the id {id}",
		status=200
		), 200

# my jokes route
@jokes.route('/mine', methods=['GET'])
def my_jokes():

	print(current_user.jokes)
	# loop through the jokes in the current user
	current_user_jokes = [model_to_dict(joke) for joke in current_user.jokes]
	print(current_user_jokes)
	
	#remove the password
	for joke in current_user_jokes:
		joke['owner'].pop('password')

	return jsonify(
		data=current_user_jokes,
		message=f"Successfully retrieved {len(current_user_jokes)} jokes.",
		status=200
		), 200