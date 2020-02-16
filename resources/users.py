import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user


# make this a blueprint
users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def test():
	return "we have a user resource"



# register route (create 'POST')
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	print(payload)

	# make username and email lowercase
	payload['username'] = payload['username'].lower()
	payload['email'] = payload['email'].lower()

	try:
		# check if the user already exists
		# if they do, we won't create the user
		models.User.get(models.User.email == payload['email'])
		# if the query doesn't cause an error, then the user exists
		print(payload['email'])

		return jsonify(
			data={},
			message="A user with that email already exists",
			status=401
			), 401

	# if we get the error, the user does not exist
	# so can proceed
	except models.DoesNotExist:
		# create user
		new_user = models.User.create(
			first_name=payload['first_name'],
			last_name=payload['last_name'],
			username=payload['username'],
			password=generate_password_hash(payload['password']),
			email=payload['email']
			)
		print("it is getting here")

		# this logs in the user and starts a session
		login_user(new_user)

		# convert the data to a dictionary
		user_dict = model_to_dict(new_user)
		print(user_dict['password'])

		# we can't jsonify the password (generated_password_hash)
		# and we don't need to send it, so we can remove it
		user_dict.pop('password')

		# return "user was created"
		return jsonify(
			data=user_dict,
			message="Successfully created a user",
			status=201
			), 201


@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	payload['email'] = payload['email'].lower()
	print(payload)


	return "you hit the login route"






